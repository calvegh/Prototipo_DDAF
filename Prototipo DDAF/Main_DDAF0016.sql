horarios ocupados:
[7, 8, 13, 10] +
horarios disponibles
[(9, '9:00'), (11, '11:00'), (12, '12:00')]
BEGIN;
--
-- Create model Cursos_Alumno
--
CREATE TABLE `curso_alumno` (`id` integer NOT NULL PRIMARY KEY, `nombre_curso` varchar(64) NOT NULL, `usuario` varchar(64) NOT NULL);
COMMIT;
