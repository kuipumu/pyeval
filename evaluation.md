## Detalles técnicos de la Solución Requerida

NOTA: Debe usar postgresql para el desarrollo de la solucion.

## Requerimientos de la API (backend)

### Endpoint: api/login

IMPORTANTE: es opcional (aunque ideal) usar un access_token (string
simple o JWT) como parte de la respuesta válida del login, que luego
seria usado en el header de todas las demás peticiones. (esta
característica tendría un alto valor cualitativo adicional en el
resultado de la evaluación).

### Endpoint: api/logs/action?q=<texto de la acción a consultar>

GET: listar los registros del log para una acción indicada
- recibe un parámetro GET con la cadena de texto a consultar
- retorna un JSON con la lista de todos los registros de logs
cuya acción conincida con el texto indicado, ordenados del más
reciente al más antiguo.
