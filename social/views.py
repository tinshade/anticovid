from django.shortcuts import render
import tweepy
def get_tweets():
	a = {'t':[]}
	api_key = "8qXBNViMseFIPsH9pxUTKM0Eg"
	api_secret_key = "GTm7ANRzW9elDfdoL0drOAymoedUMeDK9IdpIP55SPjWK2Fl5N"
	access_token = "766850384593690624-ngMv6jL3Slzc8eV2tKAlYG8MCp1OsZ9"
	access_token_secret = "PtrMuoL6pDnJ8W1xaHeiuMwqy8zFKETDwiBcsWoDH19MO"
	auth = tweepy.OAuthHandler(api_key, api_secret_key)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth, wait_on_rate_limit=True)
	search_words=['quarantine']
	for tweet in tweepy.Cursor(api.search, q=search_words, lang='en',).items(21):
		a['t'].append(tweet._json)
	return a

twcontext={
    'title':'Social Feed | COVID-19 Informatrics',
	'tweets': get_tweets()
}
def social(request):
    return render(request,'social/social.html',twcontext)
