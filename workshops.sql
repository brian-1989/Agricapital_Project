-- This script shows the workshop that is blocked at that time.
SELECT *
FROM talleres
WHERE inicio > '2021-08-15 08:00:00' AND fin < '2021-08-15 13:00:00';
