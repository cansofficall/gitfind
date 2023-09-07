import requests
from pyfiglet import figlet_format

def github_repo_finder(keyword):
    url = f"https://api.github.com/search/repositories?q={keyword}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [(repo['name'], repo['html_url']) for repo in data['items']]

    except requests.exceptions.RequestException as e:
        print(f"{keyword} için hata: {e}")
        return []

def main_menu():
    print(figlet_format('can_s_officiall repo find', font='slant'))
    
    while True:
        print("\nMenü:")
        print("1. Repo Ara")
        print("2. Çıkış")
        
        secim = input("Seçiminizi yapın: ")
        
        if secim == "1":
            keywords = input("Aranacak repo anahtar kelimelerini virgülle ayırarak girin (örn. AI, flask, django): ").split(',')
            for keyword in keywords:
                keyword = keyword.strip()
                print(f"\n{keyword.upper()} için arama sonuçları:\n")
                repos = github_repo_finder(keyword)
                if repos:
                    for name, link in repos:
                        print(f"Repo Adı: {name}\nLink: {link}\n{'-'*80}")
                else:
                    print(f"{keyword} için sonuç bulunamadı.")
        elif secim == "2":
            print("\nGörüşmek üzere bro!")
            break
        else:
            print("Geçersiz seçim!")

if __name__ == "__main__":
    main_menu()
