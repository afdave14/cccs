SELECT concat(concat(m.nameFirst, ' '), m.nameLast) AS "Full Name", 
t.teamID,
((b.H + b.BB + b.HBP) / (b.AB + b.BB + b.HBP + b.SF)) AS OBP

FROM Master m LEFT JOIN (Batting b LEFT JOIN Teams t ON b.teamID = t.teamID)
ON m.playerID = b.playerID
WHERE ((b.H + b.BB + b.HBP) / (b.AB + b.BB + b.HBP + b.SF)) <> ''
ORDER BY b.teamID