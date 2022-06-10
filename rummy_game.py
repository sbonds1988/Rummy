class Rummy:
    def __init__(self, player, cards):
        self.player = player
        self.cards = cards

    def check_meld_multiples(self, cards):
        numbers_only = []
        multiples = []
        for sublist in cards:
            numbers_only.append(sublist[0])
        for numb in numbers_only:
            if numbers_only.count(numb) >= 3:
                multiples.append(numb)
        for num in multiples:
            if multiples.count(num) >= 3:
                print("Meld card: {}".format(num))
        return multiples

    def separate_suites(self, cards):
        spades, spades_numbers = [[], []]
        hearts, hearts_numbers = [[], []]
        clubs, clubs_numbers = [[], []]
        diamonds, diamonds_numbers = [[], []]
        for card in cards:
            if card[1] == 'H':
                hearts.append(card)
            elif card[1] == 'S':
                spades.append(card)
            elif card[1] == 'D':
                diamonds.append(card)
            else:
                clubs.append(card)
        if len(spades) >= 3:
            for item in spades:
                spades_numbers.append(item[0])
        if len(hearts) >= 3:
            for item in hearts:
                hearts_numbers.append(item[0])
        if len(diamonds) >= 3:
            for item in diamonds:
                diamonds_numbers.append(item[0])
        if len(clubs) >= 3:
            for item in clubs:
                clubs_numbers.append(item[0])
        
        spades_numbers.sort()
        clubs_numbers.sort()
        hearts_numbers.sort()
        diamonds_numbers.sort()
        
        in_order_spades = []
        in_order_clubs = []
        in_order_hearts = []
        in_order_diamonds = []

        new_list = []

        new_list.append(self.check_run_melds('Hearts', hearts_numbers, in_order_hearts))
        new_list.append(self.check_run_melds('Diamonds', diamonds_numbers, in_order_diamonds))
        new_list.append(self.check_run_melds('Clubs', clubs_numbers, in_order_clubs))
        new_list.append(self.check_run_melds('Spades', spades_numbers, in_order_spades))
        return new_list

    # FUNCTION
    def check_run_melds(self, suite, suite_numbers, in_order_suite):
        if len(suite_numbers) >= 3:
            if 13 in suite_numbers and 2 in suite_numbers and 1 in suite_numbers:
                in_order_suite.append(13)
                suite_numbers.remove(13)
                in_order_suite.append(1)
                suite_numbers.remove(1)
                in_order_suite.append(2)
                suite_numbers.remove(2)
            if 12 in suite_numbers and 13 in suite_numbers and 1 in suite_numbers:
                in_order_suite.append(12)
                suite_numbers.remove(12)
                in_order_suite.append(1)
                suite_numbers.remove(1)
                in_order_suite.append(13)
                suite_numbers.remove(13)
            i = 0
            hearts_range = len(suite_numbers) - 1
            while i < hearts_range:
                if suite_numbers[i] in in_order_suite:
                    i += 1
                    break
                if (suite_numbers[i] + 1 == suite_numbers[i + 1]) and (suite_numbers[i] - 1 == suite_numbers[i-1]):
                    in_order_suite.append(suite_numbers[i])
                    in_order_suite.append(suite_numbers[i + 1])
                    in_order_suite.append(suite_numbers[i - 1])
                if in_order_suite.count(suite_numbers[i]) > 1:
                    in_order_suite.remove(suite_numbers[i])
                i += 1
        if len(in_order_suite) >= 3:
            print("You have at least one meld in {}!".format(suite))
            in_order_suite.sort()
            i = 0
            while i < len(in_order_suite):
                print("{} Meld Card: {}".format(suite, in_order_suite[i-1]))
                i += 1
        return in_order_suite

    def compare_melds(self, multiple, run):
        multiple = self.check_meld_multiples()
        run = self.separate_suites()
        for item in multiple:
            if item in run:
                print("Conundrum!")
        

player_one_cards = [[13, 'H'], [1, 'H'], [2, 'D'], [13, 'H'], [5, 'S'], [6, 'S'], [7,'C'], [13, 'D'], [7, 'S'], [1, 'D']]
player_one = Rummy('Sally', player_one_cards)
player_one.check_meld_multiples(player_one_cards)
player_one.separate_suites(player_one_cards)
#cards = player_one.compare_melds(multiples, suites)