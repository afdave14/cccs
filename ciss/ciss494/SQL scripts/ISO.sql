SELECT concat(concat(nameFirst, ' '), nameLast) AS Name, teamID, yearID,
((2B) + (2 * 3B) + (3 * HR)) / AB AS ISO
FROM Batting b JOIN Master m ON b.playerID = m.playerID
AND AB > 550
ORDER BY ISO DESC