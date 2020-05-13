# Pridict Korean's eyesight with Machine Learning 

본 자료는 연도별 시력 데이터를 활용하여 머신러닝을 활용하여 `regression` 하는 예제 입니다. 
활용을 하실 떄 어려움이 생긴다신면 `skainof23@gmail.com` 으로 연락주시길 바랍니다. 


## 자료설명 
전체 6년치 시력 데이터를  train(5년), test(1년) 로 나누어 여러 회귀 모델을 사용하여 예측하여 보았습니다.


## 환경설정
모든 자료는 `macos` 에서 만들어졌습니다. 필수적인 라이브러리의 버전을 설치 후 확인 바랍니다.

> Python version: 3.7.0 (default, Jun 28 2018, 07:39:16) 
> pandas version: 1.0.3
> matplotlib version: 3.1.3
> NumPy version: 1.18.1
> scikit-learn version: 0.22.1

```bash
> git clone https://github.com/mssung94/intel-object-detection.git
> cd Predict_Eyesight
> pip install -r requirements.txt
```

## 파일 구성 
|순서|내용|
|---|---|
|1. |년도별 데이터를 가지고 일별 데이터 만들기(좌안)|
|2. |년도별 데이터를 가지고 일별 데이터 만들기(우안)|
|3. |머신러닝으로 일별데이터 예측하기(좌안)|
|4. |머신러닝으로 일별데이터 예측하기(좌안)|


## 데이터 구성 
여기에서 활용된 자료는 아래를 참고하였습니다.
-  국가통계포털(http://kosis.kr/index/index.do): 건강검진통계 시도별 시력분포 현황