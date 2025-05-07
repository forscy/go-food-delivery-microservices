# Cara Menjalankan Project Go Food Delivery Microservices

Untuk menjalankan project Go Food Delivery Microservices ini, kita perlu mengikuti beberapa langkah. Project ini menggunakan Docker dan docker-compose untuk memudahkan proses development dan deployment.

## Prasyarat
1. Pastikan kamu sudah menginstall:
   - Docker dan Docker Compose
   - Go (versi 1.22 atau lebih tinggi)
   - Git
   - Make (opsional, untuk menjalankan Makefile commands)

## Langkah-langkah Menjalankan Project

### 1. Clone repository (jika belum)

```bash
git clone https://github.com/mehdihadeli/go-food-delivery-microservices
cd go-food-delivery-microservices
```

### 2. Jalankan infrastruktur pendukung

Project ini membutuhkan beberapa infrastruktur seperti database, message broker, dll. Kamu bisa menjalankannya dengan docker-compose:

```bash
cd deployments/docker-compose
docker-compose -f docker-compose.infrastructure.yaml up -d
```
# Menjalankan kembali tanpa tempo

```bash
docker-compose -f docker-compose.infrastructure.yaml up -d --scale tempo=0
```

Command di atas akan menjalankan semua infrastruktur yang diperlukan seperti:
- PostgreSQL
- MongoDB
- EventStoreDB
- RabbitMQ
- Redis
- dan infrastruktur lainnya

### 3. Jalankan service monitoring (opsional)

Untuk monitoring dan observability, kamu bisa menjalankan stack monitoring:

```bash
docker-compose -f docker-compose.infrastructure-collector.yaml up -d
```

Command ini akan menjalankan:
- Prometheus
- Grafana
- OpenTelemetry Collector
- dll.

### 4. Menjalankan microservices

Ada beberapa cara untuk menjalankan microservices:

#### Cara 1: Menggunakan Makefile

Dari root directory project, jalankan:

```bash
# Menjalankan catalog read service
make run-catalog-read-service

# Menjalankan catalog write service
make run-catalog-write-service

# Menjalankan order service
make run-order-service
```

#### Cara 2: Menjalankan langsung dengan Go

```bash
# Catalog read service
cd internal/services/catalogreadservice
go run main.go

# Catalog write service (buka terminal baru)
cd internal/services/catalogwriteservice
go run main.go

# Order service (buka terminal baru)
cd internal/services/orderservice
go run main.go
```

#### Cara 3: Menggunakan docker-compose untuk semua service

Kembali ke docker-compose dan jalankan:

```bash
docker-compose up -d
```

Ini akan menjalankan semua microservices beserta infrastrukturnya.

### 5. Verifikasi services berjalan

Setelah services berjalan, kamu bisa mengakses:

- Swagger UI untuk API documentation:
  - Catalog Read Service: http://localhost:8080/swagger/index.html
  - Catalog Write Service: http://localhost:8081/swagger/index.html
  - Order Service: http://localhost:8082/swagger/index.html

- RabbitMQ Management UI: http://localhost:15672 (username: guest, password: guest)
- MongoDB Express: http://localhost:8081
- Grafana (jika monitoring diaktifkan): http://localhost:3000

## Troubleshooting

1. **Jika ada error koneksi ke database atau message broker:**
   - Pastikan semua containers berjalan dengan `docker ps`
   - Periksa logs dengan `docker logs [container_name]`
   - Coba jalankan `docker-compose down` dan kemudian jalankan kembali services

2. **Jika ada issues dengan permissions atau ports:**
   - Pastikan tidak ada aplikasi lain yang menggunakan port yang sama
   - Pastikan user memiliki permission untuk menjalankan docker commands

3. **Jika ada dependency issues:**
   - Jalankan `go mod tidy` di root directory dan di setiap service directory

## Pengembangan

Untuk menambahkan fitur atau membuat perubahan:
1. Buat branch baru
2. Implementasikan perubahan
3. Jalankan tests dengan `make test` atau `go test ./...`
4. Submit pull request

Semoga berhasil menjalankan projectnya!