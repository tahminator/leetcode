from typing import List
from collections import deque

"""
topo sort, multiple entries
"""

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        This will be a slight variation of Kahn's algorithm. We still need to know how many dependencies each 
        recipe has so we know what we can cook. Whatever is in our supplies is a guaranteed entry point, so we can just 
        start with those values into the queue. The issue is knowing what child to jump to.

        I think what we can do instead is to just scan supplies and see if we have the ingredients we need to move forward.

        The key distinction is trying to figure out where Kahn's algorithm will play into this so we know what the right ordering 
        could be.
        We can use recipes and ingredients for our Kahn's algorithm; main change being that we only track the graph of recipes. Whatever we already own 
        can already just exist in our supplies set data structure anyways.
        """

        dependencies = {}
        next = {}
        ogSupplies = {}
        suppliesSet = set(supplies)
        recipeSet = set(recipes)

        for i in range(len(recipes)):
            ogSupplies[recipes[i]] = ingredients[i]

        for i in range(len(ingredients)):
            for ingredient in ingredients[i]:
                if ingredient in recipeSet:
                        children = next.get(ingredient, [])
                        children.append(recipes[i])
                        next[ingredient] = children

        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                if ingredient in recipeSet:
                    count = dependencies.get(recipe, 0)
                    count += 1
                    dependencies[recipe] = count

        q = deque()

        for i, recipe in enumerate(recipes):
            if recipe not in dependencies:
                q.append(recipe)

        res = []
        while q:
            recipe = q.popleft()
            requiredIngredients = ogSupplies.get(recipe)

            willContinue = True 
            for requiredIngredient in requiredIngredients:
                if not requiredIngredient in suppliesSet:
                    willContinue = False

            if not willContinue:
                continue

            res.append(recipe)
            suppliesSet.add(recipe)

            children = next.get(recipe, [])

            for child in children:
                count = dependencies.get(child, 1)
                count -= 1
                dependencies[child] = count

                if dependencies[child] == 0:
                    q.append(child)

        return res
 
# print(Solution().findAllRecipes(["bread"], [["yeast","flour"]], ["yeast"]))
# print(Solution().findAllRecipes(["bread","sandwich","burger"], [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], ["yeast","flour","meat"]))
