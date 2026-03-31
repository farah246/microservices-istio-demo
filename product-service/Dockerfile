FROM golang:1.21

WORKDIR /app

COPY . .

RUN go build -o product-service

EXPOSE 5002

CMD ["./product-service"]