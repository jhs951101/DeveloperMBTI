SELECT 4th, ROUND(COUNT(*) * 100 / (SELECT COUNT(*) FROM mbti), 2) as percentage
FROM mbti
GROUP BY 4th;