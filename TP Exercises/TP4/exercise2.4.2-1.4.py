def nb_racines(α, β, γ):
    Δ = (β**2) - (4*α*γ)
    if Δ > 0:
        print("La fonction a deux racines reelles")
    elif Δ == 0:
        print("La fonction a une racine reelle")
    else:
        print("La fonction na pas de racine reelle")

α = 3
β = 2
γ = 1
nb_racines(α, β, γ)
