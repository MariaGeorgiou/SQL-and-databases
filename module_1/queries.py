SELECT_ALL = 'SELECT character_id, name FROM charactercreator_character;'

AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT CC_CHAR.name, AVG(AI.weight) 
    FROM charactercreator_character AS CC_CHAR
    JOIN charactercreator_character_inventory AS CC_INV
    ON CC_CHAR.character_id = CC_INV.character_id
    JOIN armory_item AS AI 
    ON AI.item_id = CC_INV.item_id
    GROUP BY CC_CHAR.character_id
    '''