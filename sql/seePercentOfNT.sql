SELECT ROUND(COUNT(*) * 100 / (SELECT COUNT(*) FROM mbti), 2) as NT_Percentage
FROM mbti
WHERE 2nd = 'N' AND 3rd = 'T';