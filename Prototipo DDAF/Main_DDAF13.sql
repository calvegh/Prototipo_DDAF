BEGIN;
--
-- Create model CursosDDAF
--
CREATE TABLE `cursos_ddaf` (`id` integer NOT NULL PRIMARY KEY, `nombre` varchar(64) NOT NULL, `tipo` varchar(64) NOT NULL, `horario` varchar(32) NOT NULL);
COMMIT;
