from sc2.bot_ai import BotAI
from sc2.ids.unit_typeid import UnitTypeId
from sc2.position import Point2, Point3
from sc2.unit import Unit
from sc2.units import Units


class Supermente(BotAI):
    botScore = 0
    gameTime = 1900

    AttactAt = 410
    ConTodo = False

    async def on_step(self, iteration: int):
        if self.time > self.gameTime:
            print("Game Over!")
            try:
                await self.client.leave()
            except:
                print("Error al salir del juego")
                pass

        if self.time > self.AttactAt:
            await self.AtacarConTodo()
            cantidadTropas = self.units(UnitTypeId.ZERGLING).amount + self.units(UnitTypeId.DRONE).amount
            if cantidadTropas == 0:
                await self.client.leave()
        else:
            await self.recogerRecursos()
            # await self.atacar()

            await self.SlowCreaTrabajador()

            if iteration == 0:
                arrayOverlords = self.units(UnitTypeId.OVERLORD)
                if(arrayOverlords.amount > 0):
                    arrayOverlords[0].attack(self.enemy_start_locations[0])
            
            if self.units(UnitTypeId.DRONE).amount < 13:
                await self.creaTrabajador()    

            if self.supply_left < 5:
                await self.creaOverlord()

            if self.units(UnitTypeId.ZERGLING).amount > 20:
                await self.crearRoach()

            if self.units(UnitTypeId.DRONE).amount > 13:
                await self.crearZerling()

            if (self.can_afford(UnitTypeId.HATCHERY) and self.structures(UnitTypeId.HATCHERY).amount < 3) or self.minerals > 600:
                await self.expandirse()



    async def creaTrabajador(self):
        larvas = self.units(UnitTypeId.LARVA).amount
        if larvas > 0  and self.can_afford(UnitTypeId.DRONE) and self.supply_left > 0:
            self.train(UnitTypeId.DRONE)
            return True
        
        return False
    
    async def SlowCreaTrabajador(self):
        larvas = self.units(UnitTypeId.LARVA).amount
        if larvas > 0  and self.can_afford(UnitTypeId.DRONE) and self.supply_left > 0 and self.already_pending(UnitTypeId.DRONE) == 0:
            self.train(UnitTypeId.DRONE)
            return True
        
        return False

    async def creaOverlord(self):
        larvas = self.units(UnitTypeId.LARVA).amount
        if larvas > 0 and self.can_afford(UnitTypeId.OVERLORD):      
            self.train(UnitTypeId.OVERLORD)
            return True
        return False

    async def expandirse(self):
        if self.can_afford(UnitTypeId.HATCHERY):
            base = self.structures(UnitTypeId.HATCHERY)[0]
            # Buscamos un lugar libre para construir el spawning pool
            for d in range(4, 15):
                pos: Point2 = base.position.towards(self.game_info.map_center, d)
                if await self.can_place_single(UnitTypeId.HATCHERY, pos):
                    drone: Unit = self.workers.closest_to(pos)
                    drone.build(UnitTypeId.HATCHERY, pos)
        return False

    async def crearZerling(self):
        if (
            self.structures(UnitTypeId.SPAWNINGPOOL).amount
            + self.already_pending(UnitTypeId.SPAWNINGPOOL)
            == 0
        ):
            if self.can_afford(UnitTypeId.SPAWNINGPOOL):
                base = self.structures(UnitTypeId.HATCHERY)[0]
                # Buscamos un lugar libre para construir el spawning pool
                for d in range(4, 15):
                    pos: Point2 = base.position.towards(self.game_info.map_center, d)
                    if await self.can_place_single(UnitTypeId.SPAWNINGPOOL, pos):
                        drone: Unit = self.workers.closest_to(pos)
                        drone.build(UnitTypeId.SPAWNINGPOOL, pos)
            return False

        larvas = self.units(UnitTypeId.LARVA).amount
        if larvas > 0 and self.already_pending(UnitTypeId.SPAWNINGPOOL) == 0 and self.can_afford(UnitTypeId.ZERGLING) and self.supply_left > 0:
            self.train(UnitTypeId.ZERGLING, 1)        
            return True
        return False
    
    async def crearRoach(self):
        if (
            self.structures(UnitTypeId.ROACHWARREN).amount
            + self.already_pending(UnitTypeId.ROACHWARREN)
            == 0
        ):
            if self.can_afford(UnitTypeId.ROACHWARREN):
                base = self.structures(UnitTypeId.HATCHERY)[0]
                # Buscamos un lugar libre para construir el spawning pool
                for d in range(4, 15):
                    pos: Point2 = base.position.towards(self.game_info.map_center, d)
                    if await self.can_place_single(UnitTypeId.ROACHWARREN, pos):
                        drone: Unit = self.workers.closest_to(pos)
                        drone.build(UnitTypeId.ROACHWARREN, pos)
            return False

        larvas = self.units(UnitTypeId.LARVA).amount
        if larvas > 0 and self.already_pending(UnitTypeId.ROACHWARREN) == 0 and self.can_afford(UnitTypeId.ROACH) and self.supply_left > 0:
            self.train(UnitTypeId.ROACH, 1)        
            return True
        return False

    async def AtacarConTodo(self):
        if not self.ConTodo:
            # print("Atacar con todo")
            base_enemiga = self.enemy_start_locations[0]
            for unidad in self.units.not_structure:
                unidad.attack(base_enemiga)
            self.ConTodo = True

    async def expandirse(self):
        if self.can_afford(UnitTypeId.HATCHERY):
            await self.expand_now()
            return True
        return False

    async def recogerRecursos(self):
        mf: Units = self.mineral_field
        for idle_worker in self.workers.idle:
            idle_worker.gather(mf.closest_to(idle_worker))

