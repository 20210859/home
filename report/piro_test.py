import string
import random


class Player:
    def __init__(self, name, hp, damage, correct_alp):
        self.name = name  # 이름
        self.hp = hp  # 생명력
        self.damage = damage  # 데미지
        self.correct_alp = 0  # 알파벳 맞춘 횟수


class Game:

    def __init__(self):
        self.player = []  # 캐릭터의 목록. start_game()에서 생성
        self.user_character = ""  # 사용자가 선택한 캐릭터
        self.remain_alp = list(string.ascii_uppercase)  # 남은 알파벳
        self.current_str = "__________"  # 현재까지의 글자상태를 저장
        self.answer_str = ""  # 랜덤 10글자 단어

    def start_game(self):
        """
        - [ 게임 시작 전 ] 부분을 담당하는 함수 입니다.
        - 캐릭터들을 초기화 하고, 사용자가 플레이할 캐릭터를 선택합니다.
        - 랜덤 알파벳 10글자로 이루어진 answer_str 을 생성합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        self.player.append(Player("이동헌", 50, 20, 0))
        self.player.append(Player("심은서", 70, 25, 0))
        self.player.append(Player("임채은", 80, 30, 0))
        self.player.append(Player("신승현", 90, 35, 0))

        # TODO 1-(1): 사용자로부터 캐릭터를 입력받아 user_character에 저장해주세요.
        player_num = int(input('당신의 캐릭터 번호를 선택해주세요 (1,2,3,4) : '))
        self.user_character = self.player[player_num - 1]
        ##### END OF TODO 1-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

        # TODO 1-(2) : 랜덤 알파벳 10글자로 이루어진 단어를 만들어 answer_str에 저장해주세요.
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        for n in range(10):
            self.answer_str += random.choice(alpha)
        ##### END OF TODO 1-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def sort_data(self, i):
        """
        - [ 게임 진행 ] 부분에서 게임진행 순서를 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """
        # TODO 2 : 게임진행을 위한 data 를 재정렬해주세요.(ROUND 1 : 이름순, ROUND 2,3 : HP 높은 순)
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        if i == 1:
            for j in range(3):
                minIndex = j
                k = j + 1
                while k < 4:
                    if self.player[k].name < self.player[minIndex].name:
                        minIndex = k
                    k += 1

                tmp = self.player[j]
                self.player[j] = self.player[minIndex]
                self.player[minIndex] = tmp
        else :
            for j in range(3):
                minIndex = j
                k = j + 1
                while k < 4:
                    if self.player[k].hp > self.player[minIndex].hp:
                        minIndex = k
                    k += 1

                tmp = self.player[j]
                self.player[j] = self.player[minIndex]
                self.player[minIndex] = tmp
        ##### END OF TODO 2 (문제와 본 라인 사이에 코드를 작성하세요.) #####

    def play_game(self):
        """
        - [ 게임 진행 ] 부분을 담당하는 함수 입니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        print(
            f"게임은 {self.player[0].name},{self.player[1].name},{self.player[2].name},{self.player[3].name} 순으로 진행됩니다.\n")

        for i in range(4):
            if self.player[i].name == self.user_character:
                print("***** 내 캐릭터 *****")

            else:
                print(f"***** {i + 1} 캐릭터 *****")

            print(f"이름: {self.player[i].name} (HP: {self.player[i].hp})")
            # TODO 3-(1) : 플레이어와 컴퓨터의 차례에서는 랜덤의 알파벳 한글자를 선택하게 해주세요.
            # 단 앞에 나왔던 알파벳과 중복되면 안됩니다.
            ch = input('선택 알파벳 : ')
            if ch in self.answer_str:
                right = True
            else:
                right = False
            ##### END OF TODO 3-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

            # TODO 3-(2) : 정답 시, 현재까지 맞춘 단어의 상태를 출력해주세요.
            # 이 단계에서 플레이어 별 점수 집계도 처리해주셔야 합니다.
            if right == True:
                print("***** 맞았습니다 ᵔεᵔ  *****")
                for j in range(10):
                    if self.answer_str[j] == ch:
                        self.current_str = self.current_str[:j] + ch + self.current_str[j+1:]
                    print(self.current_str[j], end=' ')

                print()
                print()
                self.player[i].correct_alp += 1
            ##### END OF TODO 3-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

            # TODO 3-(3) : 오답 시, 생명력을 데미지만큼 감소시켜주고 이를 출력해주세요.
            if right == False:
                print("***** 틀렸습니다 (ﾟ⊿ﾟ)  ******")
                self.player[i].hp -= self.player[i].damage
                print(f'{self.player[i].name}님은 틀렸기 때문에 HP가 {self.player[i].hp} 남았습니다.')
                print()
            ##### END OF TODO 3-(3)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def game_result(self):
        """
        - [ 게임 종료 후 ] 부분을 담당하는 함수 입니다.
        - 게임의 결과를 생명력순, 알파벳 맞춘 횟수 순 두가지의 경우로 출력해야 합니다.
        - 동일 클래스의 game()에서 호출됩니다.
        """

        print("\n\n******************* 게임이 끝났습니다 *******************")

        # TODO 4-(1) : 생명력 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print("     게임 순위 - 생명력")
        print("=============================")
        for j in range(3):
            minIndex = j
            k = j + 1
            while k < 4:
                if self.player[k].hp > self.player[minIndex].hp:
                    minIndex = k
                k += 1

            tmp = self.player[j]
            self.player[j] = self.player[minIndex]
            self.player[minIndex] = tmp

        for i in range(4):
            if self.player[i].hp <= 0:
                self.player[i].hp = '사망'
            if self.player[i] == self.user_character:
                print(f"{i + 1}등 : *{self.player[i].name}* (HP: {self.player[i].hp})")
            else:
                print(f"{i + 1}등 : {self.player[i].name} (HP: {self.player[i].hp})")
        ##### END OF TODO 4-(1)(문제와 본 라인 사이에 코드를 작성하세요.) #####

        # TODO 4-(2) : 알파벳 맞춘 횟수 순으로 결과값을 출력해주세요.
        # 내가 선택한 캐릭터 이름 앞뒤에는 *을 붙여주세요.
        # sort 와 lambda 함수에 대해 공부해보세요. 사용하지 않아도 좋습니다.
        print("=============================")
        print(" 게임 순위 - 알파벳 맞춘 횟수")
        print("=============================")
        for j in range(3):
            minIndex = j
            k = j + 1
            while k < 4:
                if self.player[k].correct_alp > self.player[minIndex].correct_alp:
                    minIndex = k
                k += 1

            tmp = self.player[j]
            self.player[j] = self.player[minIndex]
            self.player[minIndex] = tmp
        for i in range(4):
            if self.player[i] == self.user_character:
                print(f"{i + 1}등 : *{self.player[i].name}* {self.player[i].correct_alp}회")
            else:
                print(f"{i + 1}등 : {self.player[i].name} {self.player[i].correct_alp}회")
    ##### END OF TODO 4-(2)(문제와 본 라인 사이에 코드를 작성하세요.) #####

    def game(self):
        """
        - 게임 운영을 위한 함수입니다.
        - 별도의 코드 작성이 필요 없습니다.
        """

        self.start_game()
        print("******************* 게임 시작 *******************\n")
        for i in range(1, 4):
            print("===========================")
            print(f"     ROUND {i} - START")
            print("===========================")

            self.sort_data(i)
            self.play_game()

            print("===========================")
            print(f"     ROUND {i} - END")
            print("===========================")

        self.game_result()


if __name__ == '__main__':
    """
    - 코드를 실행하는 부분입니다. 
    - 역시 별도의 코드 작성이 필요 없습니다. 
    """
    game = Game()
    game.game()