# Tentang Project Go Food Delivery Microservices

Sistem microservices untuk layanan pengiriman makanan yang dikembangkan dengan bahasa Go
## Gambaran Umum
Project "Go Food Delivery Microservices" merupakan implementasi praktis dari sistem pengiriman makanan yang dibangun menggunakan berbagai arsitektur dan teknologi modern, seperti:

- Arsitektur Microservices
- Vertical Slice Architecture
- CQRS (Command Query Responsibility Segregation)
- Domain Driven Design (DDD)
- Event Sourcing
- Event Driven Architecture
- Dependency Injection

## Fitur Utama
- Menggunakan Vertical Slice Architecture sebagai arsitektur tingkat tinggi
- Event Driven Architecture dengan RabbitMQ sebagai message broker
- Data-Centric Architecture berbasis CRUD di Catalogs Read Service
- Event Sourcing untuk layanan berbasis audit seperti Orders Service
- CQRS Pattern dan Mediator Pattern dengan library Go-MediatR
- RESTful API dengan framework Echo dan Swagger
- gRPC untuk komunikasi antar service internal
- Database: PostgreSQL, EventStoreDB, MongoDB, dan Elasticsearch
- OpenTelemetry untuk Distributed Tracing dan Metrics
- Unit Testing, End-to-End Testing, dan Integration Testing
- Docker dan docker-compose untuk deployment

## Status Project
Project ini sedang dalam pengembangan dan terus ditambahkan fitur-fitur baru dari waktu ke waktu. Project ini dapat digunakan sebagai template untuk membangun aplikasi backend microservice dengan Go.

Project ini juga memiliki versi C# yang lebih lengkap untuk referensi tambahan, dan ada juga template yang lebih sederhana bernama "go-vertical-slice-template" untuk project Golang yang tidak terlalu kompleks.

## Analisis Teknis Mendalam

### Struktur Project dan Organisasi Kode
Project ini mengikuti struktur standar Go project layout dengan modifikasi untuk mendukung pendekatan microservices. Folder utama meliputi:
1. `internal/pkg` berisi shared library untuk digunakan di semua microservices
2. `internal/services` berisi implementasi masing-masing microservice (catalogreadservice, catalogwriteservice, orderservice)
3. `deployments` berisi konfigurasi untuk Docker, Kubernetes, dan infrastruktur lainnya
4. `api` berisi definisi API dalam bentuk protobuf (untuk gRPC) dan OpenAPI/Swagger (untuk REST)

Setiap microservice menerapkan arsitektur yang sama untuk konsistensi kode, yang meliputi:
- Folder `features` yang mengelompokkan kode berdasarkan fungsionalitas bisnis
- Struktur berbasis Vertical Slice dengan endpoint, handler, command/query, dan respon dalam satu folder
- Pemisahan domain logic dari infrastruktur dan presentasi

### Analisis Arsitektur Microservices
Project mengimplementasikan "separation of concerns" secara ketat dengan memisahkan tanggung jawab antar service:
1. `catalogreadservice` - fokus pada operasi pembacaan data katalog makanan, menggunakan MongoDB untuk query yang optimal
2. `catalogwriteservice` - fokus pada operasi penulisan data katalog, menggunakan PostgreSQL untuk ACID compliance
3. `orderservice` - menangani lifecycle pesanan makanan dengan Event Sourcing untuk audit trail

Komunikasi antar service menggunakan:
- Asynchronous messaging via RabbitMQ untuk loose coupling
- gRPC untuk komunikasi synchronous yang membutuhkan performa tinggi
- Event-driven architecture untuk mendukung eventual consistency

### Implementasi Domain-Driven Design
Project menerapkan prinsip-prinsip DDD di beberapa service:
- Aggregate root seperti `Order` di orderservice
- Value objects seperti `ShopItem` untuk encapsulation
- Domain events untuk menjaga invariant dan business rules
- Repository pattern untuk abstraksi persistensi data

### Implementasi CQRS dan Event Sourcing
Penerapan CQRS dilakukan dengan:
- Pemisahan physical model untuk read dan write operations
- Penggunaan Command dan Query yang berbeda berdasarkan use case
- Mediator pattern untuk memproses command/query
- Event sourcing untuk menyimpan state changes sebagai sequence of events

### Teknologi dan Library Kunci
Analisis teknologi meliputi:
- Framework `Echo` untuk RESTful API dengan performance tinggi
- `uber-go/fx` untuk dependency injection yang robust dan maintainable
- `uber-go/zap` untuk structured logging dengan performance tinggi
- `RabbitMQ` untuk reliable message broker dengan transactional outbox pattern
- `OpenTelemetry` untuk observability dengan distributed tracing

### Tantangan Teknis dan Solusi
Implementasi microservices menghadirkan kompleksitas tersendiri:
1. Data consistency antar service ditangani dengan eventual consistency dan compensating transactions
2. Service discovery menggunakan service mesh dan service registry
3. Distributed tracing dengan OpenTelemetry untuk debuggability
4. Circuit breakers untuk fault tolerance

### Pola Testing yang Komprehensif
Project menerapkan testing strategy yang menyeluruh:
- Unit tests dengan mocking external dependencies
- Integration tests dengan testcontainers-go untuk simulasi real dependencies
- End-to-end tests untuk testing full workflows
- Load testing dengan k6 untuk performance testing

### Kemampuan Deployment dan DevOps
Project menerapkan CI/CD dan infrastruktur modern:
- Docker containers untuk portability
- Docker compose untuk development environment
- Kubernetes untuk scalable production deployment
- Prometheus dan Grafana untuk monitoring

## Kesimpulan
Project Go Food Delivery Microservices merupakan contoh implementasi modern dari sistem distributed yang menerapkan best practices dalam pengembangan microservices. Project ini tidak hanya menunjukkan cara menerapkan berbagai pattern dan arsitektur seperti CQRS, Event Sourcing, dan DDD dalam Go, tetapi juga memberikan fondasi solid untuk memahami trade-offs dalam design decisions pada sistem distributed.


