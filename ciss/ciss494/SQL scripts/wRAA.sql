SELECT concat(concat(nameFirst, ' '), nameLast) AS Name, teamID,
yearID,
ROUND(((((((wBB * (BB - IBB)) + (wHBP * HBP) + (w1B * (H - HR - 3B - 2B)) + (w2B * 2B) + (w3B * 2B) + (wHR * HR)) / (AB + BB - IBB + SF + HBP)) - wOBA) / wOBAScale) * (AB + BB + HBP + SH + SF)), 3) AS wRAA
FROM GUTS g JOIN (Batting b JOIN Master m ON b.playerID = m.playerID)
ON g.Season = b.yearID
WHERE ((wBB * BB) + (wHBP * HBP) + (w1B * (H - HR - 3B - 2B)) + (w2B * 2B) + (w3B * 2B) + (wHR * HR)) / (AB + BB - IBB + SF + HBP)  <> ''
AND AB > 50
AND yearID > 2000
ORDER BY wRAA