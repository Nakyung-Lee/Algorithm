-- 1. 최댓값 코드를 입력하세요

      SELECT MAX(DATETIME) FROM ANIMAL_INS 

-- 2. 최솟값 코드를 입력하세요

      SELECT MIN(DATETIME) FROM ANIMAL_INS

-- 3. 동물 수 코드를 입력하세요

      SELECT COUNT(*) FROM ANIMAL_INS

-- 4. 중복제거 코드를 입력하세요

      SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL

-- 5. 고양이와 개는 몇마리 있을까 코드를 입력하세요

-- GROUP BY ANIMAL_TYPE (Cat과 Dog로 그룹),  ORDER BY ANIMAL_TYPE (Cat이 Dog 보다 먼저 나와야한다)

      SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE

-- 6. 동명 동물 수 찾기 코드를 입력하세요

-- 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수를 조회
-- HAVING 은 GROUP BY가 적용된 이후에 실행됨
-- ORDER BY는 모든 데이터들을 조회가 완료된 다음, 최후에 정렬함

      SELECT NAME, COUNT(NAME) FROM ANIMAL_INS WHERE NAME IS NOT NULL GROUP BY NAME HAVING COUNT(NAME) >= 2 ORDER BY NAME
