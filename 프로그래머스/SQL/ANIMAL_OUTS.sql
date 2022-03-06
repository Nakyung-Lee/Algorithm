-- 1. 입양 시각 구하기 (1) 코드를 입력하세요
-- HOUR(DATETIME) -> 열 제목 HOUR(DATETIME) 으로 나온다 // HOUR(DATETIME) HOUR -> 열 제목 HOUR 로 나온다
-- WHERE 은 GROUP BY가 적용 전에 실행
-- WHERE 은 단일 테이블에서 데이터를 가져 오거나 여러 테이블과 결합하여 조건을 지정하는데 사용되는 SQL절

      SELECT HOUR(DATETIME) HOUR, COUNT (DATETIME) COUNT FROM ANIMAL_OUTS WHERE HOUR(DATETIME)>=9 and HOUR(DATETIME)<=19 GROUP BY HOUR ORDER BY HOUR
      
-- HAVING 은 GROUP BY가 적용 이후에 실행
-- HAVING 은 SQL select문이 집계 값이 지정된 조건을 충족하는 행만 반환하도록 지정하는 SQL절

    SELECT HOUR(DATETIME) HOUR, COUNT (DATETIME) COUNT FROM ANIMAL_OUTS GROUP BY HOUR(DATETIME) HAVING HOUR>=9 and HOUR<=19 ORDER BY HOUR
    
-- 2. 입양 시각 구하기(2) 코드를 입력하세요
-- 쿼리문에서 로컬 변수 활용
-- 대입연산자 := SQL

-- (1) 0시 ~ 23시 만들기
      SET @HOUR = -1; -- 변수 선언

      SELECT (@HOUR := @HOUR +1) AS HOUR
      FROM ANIMAL_OUTS
      WHERE @HOUR < 23;
      
-- (2) COUNT 세기
      SET @HOUR = -1; -- 변수 선언

      SELECT (@HOUR := @HOUR +1) AS HOUR,
          (SELECT COUNT(HOUR(DATETIME)) 
          FROM ANIMAL_OUTS 
          -- DATETIME 변수와 @HOUR 변수가 동일한 순간 카운트 진행
          WHERE HOUR(DATETIME)=@HOUR) AS COUNT 
          FROM ANIMAL_OUTS
      WHERE @HOUR < 23
