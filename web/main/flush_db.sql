SET FOREIGN_KEY_CHECKS=0;
DELETE FROM main_answer;
DELETE FROM main_myuser;
DELETE FROM main_profile;
DELETE FROM main_question;
DELETE FROM main_tag;
DELETE FROM main_tag_questions;
ALTER TABLE main_answer AUTO_INCREMENT = 1;
ALTER TABLE main_myuser AUTO_INCREMENT = 1;
ALTER TABLE main_profile AUTO_INCREMENT = 1;
ALTER TABLE main_question AUTO_INCREMENT = 1;
ALTER TABLE main_tag AUTO_INCREMENT = 1;
ALTER TABLE main_tag_questions AUTO_INCREMENT = 1;