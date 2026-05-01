class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #si es un caracter unico
        #si es un string vacio
        #agrupar por numero de caracteres

        #evaluar numero de palabras y agruparlas por numero
        #implementar filtro contra caracteres vacios y caracteres unicos

        groups = {}

        for s in strs:
            key = "".join(sorted(s))

            if key not in groups:
                groups[key] = []

            groups[key].append(s)

        return list(groups.values())
                    

