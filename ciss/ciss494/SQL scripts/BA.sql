SELECT concat(concat(nameFirst, ' '), nameLast) AS Name,
teamID, yearID,
(H / AB) AS AVG, (H - 2B - 3B - HR) AS 1B, 2B, 3B, HR
from Batting b join Master m
on b.playerID = m.playerID
where b.AB >= 50
order by AVG desc