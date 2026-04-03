insert into public.profession (title, description, quest_depend) values (
    'Jobless', 'An unemployed, useless piece of sh*t... Find your place in this merciless world already!', NULL
);

INSERT INTO public.attribute (title, description) VALUES
    ('Strength', 'Strength is the foundation. The more you carry, the harder you hit. If you want to dress like a tank, you’ll have to be strong.'),
    ('Dexterity', 'Dexterity — you don’t want to drop your knife or trip over a stone. Dexterity helps you deliver more precise strikes with melee weapons, dodge attacks, or use thrown weapons effectively.'),
    ('Accuracy', 'Accuracy — you want to at least hit the cans, right? The higher your accuracy, the greater the distance from which you can hit targets with firearms or thrown weapons.'),
    ('Intelligence', 'Intelligence — it’s not a good idea to be dumb when the world is ending. Intelligence helps you use more advanced technologies, tools, and weapons.'),
    ('Charisma', 'Charisma — nobody likes a jerk. Charisma affects prices with merchants and your ability to communicate with NPCs.'),
    ('Endurance', 'Endurance — in a post-apocalyptic world, you need to be able to run long distances. Endurance directly affects the number of action points in combat.'),
    ('HP', 'HP — your health must be above 0, otherwise you’re dead.'),
    ('Free Attributes', 'Free Attributes — decide which skills or traits you want to improve in yourself.'),
    ('Experience', 'You need more for get free attributes. For 1 attribute point you need 100 * summa you`r current attributes.');

insert into public.room (title, x, y, img_path, protect, mobs) values (
    'Shelter City', '0', '0', '/media/img/rooms_back/0_0.png', true, false
);

