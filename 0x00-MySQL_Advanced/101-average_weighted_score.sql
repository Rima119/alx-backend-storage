-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students

DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser()
BEGIN
    declare n int DEFAULT 0;
    declare i int DEFAULT  0;
    SELECT count(*) INTO n FROM users;
    SET i = 0;
    while i < n do
        SET @average_weighted_score = (select sum(score * weight) / sum(weight)
        FROM projects
        LEFT JOIN corrections ON projects.id = corrections.project_id
        WHERE (select id FROM users limit i, 1) = corrections.user_id);
        UPDATE users
        SET average_score = @average_weighted_score WHERE id = (SELECT id FROM users limit i, 1);
        SET i = i + 1;
    END while;
END //
DELIMITER ;
