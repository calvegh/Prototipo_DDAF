BEGIN;
--
-- Change Meta options on cursosddaf
--
--
-- Remove field capacidad from cursosddaf
--
ALTER TABLE `cursos_ddaf` DROP COLUMN `Capacidad`;
--
-- Add field tipo to cursosddaf
--
ALTER TABLE `cursos_ddaf` ADD COLUMN `tipo` varchar(64) DEFAULT b"'1'" NOT NULL;
ALTER TABLE `cursos_ddaf` ALTER COLUMN `tipo` DROP DEFAULT;
--
-- Alter field horario on cursosddaf
--
ALTER TABLE `cursos_ddaf` CHANGE `Horario` `horario` varchar(32) NOT NULL;
--
-- Alter field nombre on cursosddaf
--
ALTER TABLE `cursos_ddaf` CHANGE `Nombre` `nombre` varchar(64) NOT NULL;
--
-- Rename table for cursosddaf to (default)
--
RENAME TABLE `cursos_ddaf` TO `Main_DDAF_cursosddaf`;
COMMIT;
