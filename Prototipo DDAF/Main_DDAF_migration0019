BEGIN;
--
-- Delete model Asistencia
--
DROP TABLE `Main_DDAF_asistencia` CASCADE;
--
-- Rename field usuario on cursos_alumno to glosa_alumno
--
--
-- Rename field curso on cursos_alumno to glosa_curso
--
--
-- Add field id_alumno to cursos_alumno
--
ALTER TABLE `curso_alumno` ADD COLUMN `id_alumno` integer DEFAULT 1 NOT NULL;
ALTER TABLE `curso_alumno` ALTER COLUMN `id_alumno` DROP DEFAULT;
--
-- Add field id_curso to cursos_alumno
--
ALTER TABLE `curso_alumno` ADD COLUMN `id_curso` integer DEFAULT 2 NOT NULL;
ALTER TABLE `curso_alumno` ALTER COLUMN `id_curso` DROP DEFAULT;
COMMIT;
