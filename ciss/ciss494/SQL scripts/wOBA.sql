SELECT yearID, teamID,
concat(concat(nameFirst, ' '), nameLast) AS Name,
((wBB * (BB - IBB)) + (wHBP * HBP) + (w1B * (H - HR - 3B - 2B)) + (w2B * 2B) + (w3B * 2B) + (wHR * HR)) / (AB + BB - IBB + SF + HBP) AS wOBA
FROM GUTS g JOIN (Batting b JOIN Master m ON b.playerID = m.playerID)
ON g.Season = b.yearID
WHERE ((wBB * BB) + (wHBP * HBP) + (w1B * (H - HR - 3B - 2B)) + (w2B * 2B) + (w3B * 2B) + (wHR * HR)) / (AB + BB - IBB + SF + HBP) <> ''
AND yearID > 2000
AND AB > 50
ORDER BY wOBA DESC