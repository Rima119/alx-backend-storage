-- SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student

DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
	IN user_id INT
)
BEGIN
    SET @average_weighted_score = (SELECT sum(score * weight) / sum(weight)
    FROM projects
    LEFT JOIN corrections ON projects.id = corrections.project_id
    WHERE corrections.user_id = user_id);
    UPDATE users
    SET average_score = @average_weighted_score WHERE id = user_id;
END //
DELIMITER ;
