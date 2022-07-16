## Initialization
# 1) This game is designed for two players.  Initially each player is dealt
# half a standard deck (26 cards)

## Gameplay
# 2) Check if either player has zero cards in either their deck or discard
# pile.  If either player does have zero cards, in either collectoin the
# game is over and that player loses
# 3) Each player flips the top card of their deck onto the "table."  If the
# cards have different ranks (regardless of suit) go to step 4a.  If the
# cards have the same rank, go to step 4b.
# 4a) The player who has flipped the higher ranking card coollects all
# cards in the common area and adds them to their discard pile
# 4b) Each player flips the top card of their deck onto the "table,"
# face down.  In practice, this means that neither this card's rank
# nor suit matters.  Return to Step 3.

## Necessary imports
from sys import path as pythonpath
pythonpath.append('../')
from common.cards import Card, CardCollection
from war.player import WarPlayer

def play_war(
        index = 1, # To keep seperate log files if desired
        debug = False
    ):

    ## Initialize a new deck and new players
    deck = CardCollection()
    deck.new_deck()
    deck.shuffle()
    playerA = WarPlayer()
    playerB = WarPlayer()

    ## Split the deck between the playesr
    splits = deck.split(num_split=2)
    playerA.deck.add_cardcollection(splits[0])
    playerB.deck.add_cardcollection(splits[1])

    # Avoid confusion later - we're done with these
    del splits

    # Basic metadata
    num_turn = 1
    game_over = False

    if debug:
        log_filename = "logs/{index:06d}.csv".format(index=index)
        log_file = open(log_filename, "w")
        header = "Num A Controlled,Num B Controlled," + \
                 "A Played,B Played,Reshuffled,B Reshuffled\n"
        log_file.write(header)

    # Gameplay loop
    while not game_over:
        # Flip cards face-up
        playerA.flip()
        playerB.flip()

        # Used in debugging (if applicable)
        A_played = playerA.peek_active()
        B_played = playerB.peek_active()
        A_wins_round = (A_played > B_played)
        B_wins_round = (B_played > A_played)
        tie_round = not (A_wins_round or B_wins_round)

        if A_wins_round:
            # Add both players' active areas to playerA's discard pile
            # and empty both players' active areas
            playerA.discard.add_cardcollection(playerA.empty("active"))
            playerA.discard.add_cardcollection(playerB.empty("active"))

        if B_wins_round:
            # Add both players' active areas to playerB's discard pile
            # and empty both players' active areas
            playerB.discard.add_cardcollection(playerA.empty("active"))
            playerB.discard.add_cardcollection(playerB.empty("active"))

        if debug:
            log_line = "{A_controlled},{B_controlled}," \
            "{A_played},{B_played},{A_reshuffled},{B_reshuffled}\n".format(
                A_controlled = playerA.get_controlled(),
                B_controlled = playerB.get_controlled(),
                A_played = A_played,
                B_played = B_played,
                A_reshuffled = ["", "X"][A_wins_round],
                B_reshuffled = ["", "X"][B_wins_round]
            )
            log_file.write(log_line)

        if tie_round:
            # The rank of both cards is equal - flip another card "face down" (it
            # identity will never be referenced, but can be moved between decks)
            playerA.flip()
            playerB.flip()

        num_turn += 1
        # TODO - Add other game over / victory conditions
        game_over = playerA.get_controlled() == 52 or \
                    playerB.get_controlled() == 52

    if debug:
        log_file.close()

    # Basic checks
    assert playerA.active.get_length() == 0
    assert playerB.active.get_length() == 0
    assert playerA.get_controlled() != playerB.get_controlled()
    assert (playerA.get_controlled() + playerB.get_controlled()) == 52

    return num_turn