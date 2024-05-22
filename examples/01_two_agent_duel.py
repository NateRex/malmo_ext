from malmoext import *
from malmoext.agent import Agent

class TwoAgentDuel(Scenario):

    def build_scenario(self, builder):
        
        # Metadata
        builder.set_description('Two Agent Duel')
        builder.set_time_limit(30)
        builder.set_time_of_day(TimeOfDay.Sunset)

        # Agents
        builder.add_agent('agent1', AgentType.CPU)
        builder.add_agent('agent2', AgentType.Human)
        builder.agents['agent1'].set_position(Vector(0, 4, 0))
        builder.agents['agent2'].set_position(Vector(10, 4, 0))
        builder.agents['agent1'].add_inventory_item(Item.All.diamond_sword, Inventory.HotBar._0)
        builder.agents['agent2'].add_inventory_item(Item.All.diamond_sword, Inventory.HotBar._0)

        # Structures
        builder.world.add_cube(Block.Stone, Vector(-100, 3, -100), Vector(100, 30, 100))
        builder.world.add_cube(Block.Air, Vector(-99, 4, -99), Vector(99, 29, 99))
        for i in range(-99, 99):
            for j in range(-99, 99):
                if i % 4 == 0 and j % 4 == 0:
                    builder.world.add_block(Block.Torch, Vector(i, 4, j))

    def on_tick(self, agents) -> None:
        print(agents['agent1'].to_json())

# Run scenario
scenario = TwoAgentDuel()
scenario.run(ports=[10000, 10001])