SET FOREIGN_KEY_CHECKS=0;
DELETE FROM main_answer;
DELETE FROM auth_user;
DELETE FROM main_profile;
DELETE FROM main_question;
DELETE FROM main_tag;
DELETE FROM main_tag_questions;
DELETE FROM main_like;
DELETE FROM main_answerlike;
DELETE FROM main_questionlike;
ALTER TABLE main_answer AUTO_INCREMENT = 1;
ALTER TABLE auth_user AUTO_INCREMENT = 1;
ALTER TABLE main_profile AUTO_INCREMENT = 1;
ALTER TABLE main_question AUTO_INCREMENT = 1;
ALTER TABLE main_tag AUTO_INCREMENT = 1;
ALTER TABLE main_tag_questions AUTO_INCREMENT = 1;
ALTER TABLE main_like AUTO_INCREMENT = 1;
ALTER TABLE main_answerlike AUTO_INCREMENT = 1;
ALTER TABLE main_questionlike AUTO_INCREMENT = 1;