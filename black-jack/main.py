import random
from art import logo

def play_blackjack():
    def draw_card(deck):
        return random.choice(deck)

    def calculate_total(hand):
        total = sum(hand)
        if 11 in hand and total > 21:
            hand[hand.index(11)] = 1
            total = sum(hand)
        return total

    def determine_winner(player_total, dealer_total):
        if dealer_total > 21:
            return "Dealer busts! You win!"
        elif player_total > 21:
            return "You busted! Dealer wins."
        elif player_total == dealer_total:
            return "It's a tie!"
        elif player_total == 21 and dealer_total != 21:
            return "Blackjack! You win!"
        elif dealer_total == 21:
            return "Dealer has Blackjack. You lose."
        elif player_total > dealer_total:
            return "You win!"
        else:
            return "Dealer wins."
    
    def display_hands(player, dealer, reveal_dealer=False):
        print(f"Your cards: {player}, total: {calculate_total(player)}")
        if reveal_dealer:
            print(f"Dealer's cards: {dealer}, total: {calculate_total(dealer)}")
        else:
            print(f"Dealer's first card: {dealer[0]}")
    
    print(logo)
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]
    
    display_hands(player_hand, dealer_hand)
    
    while calculate_total(player_hand) < 21:
        action = input("Type 'y' to hit, 'n' to stand: ").strip().lower()
        if action == 'y':
            player_hand.append(draw_card(deck))
            display_hands(player_hand, dealer_hand)
        else:
            break
    
    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)
    
    while dealer_total < 17:
        dealer_hand.append(draw_card(deck))
        dealer_total = calculate_total(dealer_hand)
    
    display_hands(player_hand, dealer_hand, reveal_dealer=True)
    print(determine_winner(player_total, dealer_total))
    
    if input("Play again? (y/n): ").strip().lower() == 'y':
        play_blackjack()
    else:
        print("Thanks for playing! Goodbye.")

play_blackjack()
