# [블록체인 프로그래밍 프로젝트]

```
A Blockchain-based Product Ownership Tracking System
2022 2년 학기
```
1. 개요
어떤 물품 예 자동차나 명품 등 중고 거래가 이루어지는 제품 의 최초 구매자로( : )
부터 이후 번째 소유자 번째 소유자 등으로 이어지는 물품의 소유권 이전 내용 2 , 3
을 블록체인에 기록하면 특정 물품의 매매 시 현재의 소유자 전체 소유권 이전 , , ,
히스토리 실거래 가격 변동 추이 등에 대한 신뢰할 수 있는 정보를 거래 당사자 ,
양측이 확인할 수 있다 이러한 서비스를 제공하는 블록체인 이하. ( myBlockChain이
라 함 기반의 물품 소유권 추적 시스템을 설계 및 구현하되 학부 수업의 과제로 ) ,
제시된 프로젝트임을 고려하여 시스템의 복잡도를 낮추고 핵심 기능의 구현에 집중
하도록 여러 가정과 제한을 둔다.
2. P2P 네트워크
myBlockChain을 위한 네트워크는 다수의 노드들과 다수의 사용자 노드P2P full
들로 구성된다 이 네트워크는 단일 컴퓨터상의 가상 네트워크로 실현되는데. P2P ,
각 노드는 각기 하나의 process , 로 링크로 연결된 두 노드 사이의 통신은 process
사이의 IPC 방식으로 구현된다. P2P 네트워크의 위상(topology)은 파일
topology.dat에 기술된 것처럼 정해진다 파일의 예는 다음과 같으며 여기서. , F는
full , U노드 는 사용자 노드, U-F는 U와 F사이의 링크, F-F는 F와 F 사
이의 링크를 의미한다.

% cat topology.dat
{
node F0, F1, F2, F3, F4, F
node U0, U1, U2, U
link U0-F1, U1-F2, U2-F4, U3-F
link F0-F1, F2-F1, F2-F4, F3-F4, F4-F0, F4-F1, F3-F1, F2-F5, F4-F
}
%

사용자 노드는 물품의 소유권 이전을 위한 거래 트랜잭션( (transaction)으로 표현)
를 발생시켜 이를 자신과 연결된 노드 사용자 노드는 하나의 노드에만 연결full ( full
된다고 가정 에 전달한다 사용자 노드는 하나의 노드에만 연결된다고 가정한). full
다 각 노드는 수신한 트랜잭션을 검증하는데 검증 성공 라 판단 하면 저. full , (valid )
장한 후 이를 이웃 노드 들 에 보내고 각 이웃 노드는 이를 다시 이웃 들 에 전파, ( ) , ( )
하는 식으로 전체 네트워크에 전파되게 한다. Full 노드는 자신이 판단하는 longest
chain의 마지막 블록에 연결할 블록을 채굴하는데 이 과정에서 채굴에 먼저 성공,


하기 위해 다른 노드들과 경쟁한다full. Full 노드는 채굴 성공 시 채굴 블록을 즉,
시 이웃 노드 들 에 전달해 이 블록이 전체 네트워크로 전파되게 한다( ).

3. 트랜잭션 구성 및 발생
이 서비스에서 필요한 트랜잭션은 단 한 가지 종류로 판매자(seller)가 구매자
(buyer)에게 물품의 소유권을 넘기는 거래 내용을 기록한 것이다 트랜잭션은. trID:
<input, output, identifier, modelNo, manufactured date, price, trading date,
others>로 구성되는데, input은 특정 물품의 판매자 현재 해당 물건의 소유자 의 ( )
public key , output이며 은 이 물품 구매자의 public key. 이다 또한 identifier(특정
물품을 지칭하는 예를 들어 물품에 부착된 ID( , bar-code QR- code 나 통해 얻는
값)), modelNo(물품의 모델명), manufactured date(물품의 제조일 은 이 물품의 모)
든 과거 및 현재와 미래의 판매 트랜잭션들에서 값이 변할 수 없는 immutable , 이며
price(판매된 가격), trading date(거래일 와 ) others mutable. others 는 이다 필드는
이 물품에 대한 설명으로 어떤 내용이든 쓸 수 있다 예를 들어 물품에 어떤 훼손( ,
이 생긴 경우 판매 시 이를 명시할 수 있음 물품 거래 값을 받고 물품 넘김 는 오). ( )
프라인으로 이루어짐을 가정하며 따라서 트랜잭션은 물품값 전달의 목적이 아니라 ,
이 거래의 내용을 정확히 기록으로 남기는 목적으로만 사용한다 는 트랜잭션의. trID
ID로서 트랜잭션 전체 서명 제외 에 대한 해시 함수 적용 결과이다 트랜잭션은 판( ).
매자와 구매자의 확인 후 판매자의 트랜잭션 전체에 대한 서명이 추가된 상태로 ,
P2P 네트워크에 전파된다 이 서명은 판매자의. public key로 검증할 수 있다.
트랜잭션은 각 사용자 노드 U에서 우선 임의로 적절한 수 예 의 최초 차 판( : 3) (1 )
매 트랜잭션을 발생시키고 이후 적절한 시간 간격을 두고 예 초 자신이 생성한 , ( : 10 )
물품(identifier로 구분 의 차 판매 차 판매 를 발생시킨다 이때 여러 사용자 ) 2 , 3 , ....
노드들이 서로 같은 물품 즉( , identifier가 같은 물품 을 판매하는 트랜잭션을 발생시)
키지 않도록 한다(identifier 크기가 충분히 크고 이를 랜덤하게 생성하면 그와 같,
은 확률은 무시할 수 있음 이런 과정을 통해 각 사용자 노드는 적절한 수의 물품). ,
들에 대해 최초 차, , 1 , ... , k차 판매 트랜잭션을 발생시켜 이들을 포함한 블록을
full 노드들이 채굴할 수 있도록 한다 트랜잭션의 내용은. , (k-1)차 판매의 구매자가
k차 판매의 판매자와 같으며 mutable 필드 값들은 변하지 않도록 하면서 자유롭게 ,
값을 부여한다.
4. 블록 구조
블록은 헤더와 나머지 부분으로 구성되는데 헤더에는 , blockNo(myBlockChain 상
의 블록 순서로서 genesis block blockNo 0, 은 로 다음 블록은 1, ... No의 를 가
짐), prevHash(myBlockChain 상 직전 블록에 대한 hash pointer), nonce(hash
puzzle 풀 때 이를 변경시키며 , target number보다 블록 hash 결과가 작아질 때까
지 시도함 및 ) Merkle-root(트랜잭션들을 로 가지는 leaf Merkle-tree root의 에 해당


하는 hash )값 으로 구성되며 나머지 부분은 이 블록에 포함될 트랜잭션들을 , leaf
들로 하는 Merkle-tree ( Bitcoin이다 다만 과는 다르게 coinbase 트랜잭션은 없음).

5. 채굴 및 myBlockChain 형성
full 각 노드는 채굴을 위해 블록에 포함될 트랜잭션들을 모두 검증하는데 검증,
을 위한 과정은 다음과 같다 트랜잭션. 에 대하여, (1) 를 통해 판매하려는 물
품의 최종 소유자 즉 합의된 마지막 판매의 구매자 가 ( ) 의 input(즉 판매자 과 같은)
지, (2) 의 immutable 필드들 값이 합의된 마지막 판매의 그것들과 일치하는지,
(3) 서명이 의 input 주소인 public key로 검증한 결과  (전체 서명 제외한 의 서)
명이 맞는지 확인한다 그리고 검증을 통과한 트랜잭션들을 선택해 ,. Merkle-tree를
구성하고 블록 헤더의 , nonce 값을 차례로 변경하면서 target number보다 작아질
때까지 반복한다 채굴에 성공한 노드는 채굴한 블록을 즉시. full P2P 네트워크의
다른 노드들에게 전파한다 사용자 노드는 도착한 채굴 블록을 무시하도록 하거나( ,
아예 F->U 방향의 통신을 차단함 채굴된 블록을 수신한 노드는 이 블록을 ). full
검증한 후 이 블록을 반영한 갱신된 , myBlockChain에 기반하여 새로운 블록의 채
굴을 시도한다.
Bitcoin과 달리 이러한 채굴 과정의 난도, (difficulty)는 불변이라 가정하고 target
number 역시 고정된 값을 사용한다 이때. target number는 블록 채굴에 소요되는
평균 시간이 초 초 정도가 되도록 자유롭게 정하고 예를 들어 비트의 (10 ~15 ) ( 256
target number 000000000010...0가 이라고 하면 해시 적용 후 결과가 개의 으, 11 0
로 시작되면 성공 이를 모든 노드들이 적절한 방법으로 알게 한다), full.
myBlockChain Bitcoin longest chain rule은 의 을 따라 각 노드가 현재 합의된 full
chain이 무엇인지를 독자적으로 판단하고 이를 바탕으로 다음 채굴될 블록을 어느 ,
블록에 연결할 것인지 결정하게 한다 따라서. Bitcoin 블록체인과 마찬가지로 일정
기간 노드 사이의 합의된 체인에 대한 의견 불일치가 있을 수 있지만 궁극적full ,
으로 모든 노드들 사이에 합의된 가장 긴 full , myBlockChain이 존재할 것이다.
6. 마스터 process를 통한 동작 확인
구현된 프로그램이 요구 사항을 모두 만족시키는지 확인하기 위해 질의를 받고 ,
그에 대한 응답을 구하여 보여주는 역할을 하는 마스터 process를 생성한다 이.
process myBlockChain 는 및 모든 노드들에 접근하여 필요한 데이터를 추출하full
거나 요청하여 받을 수 있다. Full 노드를 구현한 process는 마스터 process의 데
이터 요청에 대하여 즉각적으로 응하여 해당 데이터를 제공해야 한다.
마스터 process를 통해 확인할 수 있는 동작의 종류는 다음과 같다.

(1) snapshot myBlockChain ALL(또는 특정 F)
ALL이 지정되면 현재 시점의 각 노드가 판단하는 full myBlockChain , 을 특정 F
가 지정되면 해당 F가 판단하는 myBlockChain , 을 각각 다음과 같이 출력한다.


## (출력 형태는 내용을 이해하기 쉽도록 배치한다면 아래와 일치하지 않아도 좋음)

F0 : blockNo 0 blockNo 1... blockNo n
// 헤더 내용 헤더 내용 헤더 내용// //
// M tree trID( ->의 좌 우 순서 들 ) // M tree trID // M tree trID의 들 의 들
F1 : blockNo 0 blockNo 1... blockNo n
// 헤더 내용 헤더 내용 헤더 내용// //
// M tree trID( ->의 좌 우 순서 들 ) // M tree trID // M tree trID의 들 의 들
...

(2) snapshot trPool <F>
Full F노드 가 현재 유지하고 있는 트랜잭션 풀 채굴 시 블록에 포함될 수 있는 (
트랜잭션들의 집합 의 내용을 다음과 같이 출력한다 출력 형태는 내용을 이해하기 ). (
쉽도록 배치한다면 아래와 일치하지 않아도 좋음)

F :
trID input= xxx ... , output= yyy ...
identifier= www ... , modelNo= yyy ... , manufactured date= zzz ... ,
price= aaa ... , trading date= bbb ... , others= ccc ...
trID’ input= abc ... , output= def ...
identifier= uuu ... , modelNo= vvv ... , manufactured date= ttt ... ,
price= ghi ... , trading date= jkl ... , others= mno ...
...

(3) verifyLastTr <F>
Full 노드 F가 가장 최근의 블록 채굴 시 포함한 마지막 트랜잭션의 검증 결과
( , F즉 가 가장 최근 시도한 채굴 시 성공 여부 무관 사용한 블록에 마지막으로 포( )
함된(Merkle tree rightmost leaf의 에 해당하는 트랜잭션에 대한 검증 내용 및 결)
과 를 다음과 같이 출력한다 출력 형태는 내용을 이해하기 쉽도록 배치한다면 아). (
래와 일치하지 않아도 좋음)

F : trID
last transaction’s output : xxxxx ... // 이 물품에 대한 직전 거래 관련
trID’s input : xxxxx ...
last transaction’s
identifier= www ... , modelNo= yyy ..., manufactured date= zzz ...
trID’s
identifier= www ... , modelNo= yyy ..., manufactured date= zzz ...


trID’s signature: abcdef..... verifying using trID’s input: pqrst....
verified successfully!!

(4) trace <identifier> ALL(또는 자연수 )
identifier해당 의 물품에 대한 거래 내용 트랜잭션을 최근부터 시작하여 모두(ALL
인 경우 또는 ) 개 만큼 다음과 같이 출력하라 출력 형태는 내용을 이해하기 쉽. (
도록 배치한다면 아래와 일치하지 않아도 좋음)

[blockNo 31, trID: ...] [blockNo 26, trID’: ...] ...
// trID 트랜잭션 내용 // trID’ 트랜잭션 내용 ...
