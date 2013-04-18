SELECT concat(concat(nameFirst, ' '), nameLast) AS Name, teamID, yearID,
(H - HR) / (AB - SO - HR + SF) AS BABiP
FROM Batting b JOIN Master m ON b.playerID = m.playerID
WHERE (H - HR) / (AB - SO - HR + SF) <> ''
AND AB > 50
ORDER BY BABiP DESC