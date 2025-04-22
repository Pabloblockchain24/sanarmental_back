# 📘 Documentación de Modelos: Clínica de Salud Mental

Este proyecto contiene los modelos principales para gestionar pacientes, profesionales y consultas en una clínica de salud mental.

---

## 📌 Modelos Principales

### 🧑‍⚕️ Profesional

Representa a un profesional de la salud mental (psicólogo/a).

| Campo              | Tipo              | Descripción                                     |
|--------------------|-------------------|-------------------------------------------------|
| `id`               | AutoField         | ID único del profesional                        |
| `nombre`           | CharField         | Nombre del profesional                          |
| `apellido`         | CharField         | Apellido del profesional                        |
| `rut`              | CharField         | RUT del profesional                             |
| `fecha_nacimiento` | DateField         | Fecha de nacimiento                             |
| `tipo_atencion`    | CharField         | Presencial u Online                             |
| `especialidad`     | CharField         | Especialidad del profesional                    |
| `direccion`        | CharField         | Dirección física (si aplica)                    |
| `telefono`         | CharField         | Teléfono de contacto                            |
| `correo`           | EmailField        | Correo electrónico                              |
| `imagen`           | ImageField        | Imagen del profesional                          |

📎 **Relaciones**:
- Un **Profesional** puede tener **muchas Consultas** (`related_name="consultas"` desde el modelo `Consulta`).

---

### 🧍 Paciente

Representa a un paciente registrado en el sistema.

| Campo              | Tipo              | Descripción                                     |
|--------------------|-------------------|-------------------------------------------------|
| `id`               | AutoField         | ID único del paciente                           |
| `nombre`           | CharField         | Nombre del paciente                             |
| `apellido`         | CharField         | Apellido del paciente                           |
| `rut`              | CharField         | RUT del paciente                                |
| `fecha_nacimiento` | DateField         | Fecha de nacimiento                             |
| `sexo`             | CharField         | M, F u O (Otro)                                 |
| `direccion`        | CharField         | Dirección de residencia                         |
| `telefono`         | CharField         | Teléfono de contacto                            |
| `correo`           | EmailField        | Correo electrónico                              |
| `imagen`           | ImageField        | Imagen del paciente                             |
| `motivo_consulta`  | CharField         | Descripción del motivo de consulta              |
| `objetivos`        | CharField         | Objetivos terapéuticos                          |

📎 **Relaciones**:
- Un **Paciente** puede tener **muchas Consultas** (`related_name="consultas"` desde el modelo `Consulta`).

---

### 📅 Consulta

Representa una sesión agendada entre un paciente y un profesional.

| Campo        | Tipo        | Descripción                                   |
|--------------|-------------|-----------------------------------------------|
| `id`         | AutoField   | ID único de la consulta                       |
| `fecha`      | DateField   | Fecha de la consulta                          |
| `hora`       | TimeField   | Hora de la consulta                           |
| `estado`     | CharField   | Agendada, Confirmada, Completada o Cancelada |
| `evolucion`  | CharField   | Notas sobre la evolución del paciente         |
| `profesional`| ForeignKey  | Profesional asociado a la consulta            |
| `paciente`   | ForeignKey  | Paciente asociado a la consulta               |

📎 **Relaciones**:
- Cada **Consulta** pertenece a **un Profesional** y **un Paciente**.
- Estas relaciones se definen con `ForeignKey`, y se puede acceder a las consultas desde los modelos relacionados mediante:
  ```python
  profesional.consultas.all()
  paciente.consultas.all()
