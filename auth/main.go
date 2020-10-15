package main

import (
	"github.com/dgrijalva/jwt-go"
	"github.com/gin-gonic/gin"
	"log"
	"os"
	"time"
)

func main() {

	r := gin.Default()
	r.GET("/token", func(c *gin.Context) {
		email := c.Query("email")
		token, err := GetToken(email)
		if err != nil{
			log.Fatal("Error after getting token for email")
		}
		c.JSON(200, gin.H{
			"token": token,
		})
	})
	r.Run()
}

func GetToken(email string) (string, error){
	claims := jwt.MapClaims{}
	claims["authorized"] = true
	claims["email"] = email
	claims["exp"] = time.Now().Add(time.Hour * 15).Unix()
	at := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
	//FIRMAMOS EL TOKEN CON UN SECRET PASADO POR VARIABLE DE ENTORNO
	token, err := at.SignedString([]byte(os.Getenv("SECRET")))
	if err != nil {
		return "", err
	}
	return token, nil
}