SELECT  RI.REST_ID
,       RI.REST_NAME
,       RI.FOOD_TYPE
,       RI.FAVORITES
,       RI.ADDRESS
,       ROUND(AVG(RR.REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO RI
LEFT JOIN REST_REVIEW RR
ON RI.REST_ID = RR.REST_ID
WHERE RR.REVIEW_SCORE IS NOT NULL
GROUP BY RI.REST_ID, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS
HAVING RI.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, RI.FAVORITES DESC
