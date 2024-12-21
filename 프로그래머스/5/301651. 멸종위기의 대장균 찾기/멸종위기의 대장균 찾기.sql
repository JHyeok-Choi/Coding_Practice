WITH RECURSIVE GEN(ID, PARENT_ID, GENERATION) AS
(
    SELECT  ID
    ,       PARENT_ID
    ,       1 AS GENERATION
    FROM ECOLI_DATA
    WHERE PARENT_ID IS NULL
    
    UNION ALL
    
    SELECT  ED1.ID
    ,       ED1.PARENT_ID
    ,       GEN.GENERATION + 1 AS GENERATION
    FROM GEN
    
    INNER JOIN ECOLI_DATA ED1
    ON GEN.ID = ED1.PARENT_ID
)

SELECT  COUNT(*) AS COUNT
,       GENERATION
FROM GEN G1
LEFT JOIN ECOLI_DATA ED
ON G1.ID = ED.PARENT_ID
WHERE ED.PARENT_ID IS NULL
GROUP BY GENERATION
