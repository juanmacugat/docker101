FROM golang:1.14-alpine AS build
ARG APP_VERSION=development

WORKDIR /src

#COPY vendor ./vendor
COPY go.mod go.sum ./

COPY . .

RUN go build -mod=vendor

FROM alpine
WORKDIR /app
COPY --from=build /src/auth .
ENTRYPOINT ["./auth"]
EXPOSE 8080

