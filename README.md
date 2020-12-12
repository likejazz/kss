# python-kss

## Objective
- 박상길님의 KSS(Korean Sentence Splitter)는 cython으로 구현되어있다.
- Cython의 빠른 속도는 장점이지만 `cythonize`때문에 cython이 설치된 환경에서만 설치 가능하다.
- 이 때문에 현재의 KSS는 프로젝트 디펜던시에 추가하기 매우 까다롭다.
- 이러한 문제를 해결하기 위해 순수 파이썬만 이용하여 KSS를 재구현한다.
<br><br>

## Install
- pip를 이용하여 설치할 수 있다.
```console
pip install python-kss
```
<br><br>

## Usage
- 기존 KSS 사용법과 100% 동일하다.
```python
import kss

s = "회사 동료 분들과 다녀왔는데 분위기도 좋고 음식도 맛있었어요 다만, 강남 토끼정이 강남 쉑쉑버거 골목길로 쭉 올라가야 하는데 다들 쉑쉑버거의 유혹에 넘어갈 뻔 했답니다 강남역 맛집 토끼정의 외부 모습."
for sent in kss.split_sentences(s):
    print(sent)
```
```
회사 동료 분들과 다녀왔는데 분위기도 좋고 음식도 맛있었어요
다만, 강남 토끼정이 강남 쉑쉑버거 골목길로 쭉 올라가야 하는데 다들 쉑쉑버거의 유혹에 넘어갈 뻔 했답니다
강남역 맛집 토끼정의 외부 모습.
```
<br><br>

## Reference
- [KSS 깃허브 레포](https://github.com/likejazz/korean-sentence-splitter)
- [KSS 도큐먼트](http://docs.likejazz.com/kss/)
- [형태소분석기에 탑재된 문장 분리기 분석](http://semantics.kr/%ed%95%9c%ea%b5%ad%ec%96%b4-%ed%98%95%ed%83%9c%ec%86%8c-%eb%b6%84%ec%84%9d%ea%b8%b0-%eb%b3%84-%eb%ac%b8%ec%9e%a5-%eb%b6%84%eb%a6%ac-%ec%84%b1%eb%8a%a5%eb%b9%84%ea%b5%90/)

