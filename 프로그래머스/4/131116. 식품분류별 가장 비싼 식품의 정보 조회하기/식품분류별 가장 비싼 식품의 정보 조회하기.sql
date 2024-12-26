SELECT  FP1.CATEGORY
,       FP1.PRICE AS MAX_PRICE
,       FP1.PRODUCT_NAME
FROM FOOD_PRODUCT FP1
LEFT JOIN FOOD_PRODUCT FP2
ON FP1.CATEGORY = FP2.CATEGORY AND FP1.PRICE < FP2.PRICE
WHERE FP2.PRODUCT_ID IS NULL
AND FP1.CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY FP1.PRICE DESC
