DELIMITER //

CREATE TRIGGER track_evidence_changes
AFTER INSERT ON evidence
FOR EACH ROW
BEGIN
    INSERT INTO evidence_changes (evidence_id, action, change_date)
    VALUES (NEW.evidence_id, 'INSERT', NOW());
END;
//
-- Reset the delimiter
DELIMITER ;

# insert value for testing trigger
insert into evidence values (12, 'Document B');

# display evidence changes to check if trigger worked
SELECT * FROM capevidence.evidence_changes;
