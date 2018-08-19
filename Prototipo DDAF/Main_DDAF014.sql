BEGIN;
--
-- Add field días to cursosddaf
--
ALTER TABLE `cursos_ddaf` ADD COLUMN `días` varchar(32) DEFAULT b"'1'" NOT NULL;
ALTER TABLE `cursos_ddaf` ALTER COLUMN `días` DROP DEFAULT;
--
-- Add field pista to cursosddaf
--
ALTER TABLE `cursos_ddaf` ADD COLUMN `pista` integer DEFAULT 1 NOT NULL;
ALTER TABLE `cursos_ddaf` ALTER COLUMN `pista` DROP DEFAULT;
--
-- Add field profesor to cursosddaf
--
ALTER TABLE `cursos_ddaf` ADD COLUMN `profesor` varchar(64) DEFAULT b"'1'" NOT NULL;
ALTER TABLE `cursos_ddaf` ALTER COLUMN `profesor` DROP DEFAULT;
--
-- Alter field horario on cursosddaf
--
ALTER TABLE `cursos_ddaf` MODIFY `horario` integer NOT NULL;
COMMIT;
