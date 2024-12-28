from django.core.cache import cache


class CacheGETMiddleware:

    def __init__(self,get_response):

        self.get_response=get_response #get the response




    def __call__(self,request):

        if request.method == "GET": #checking if the request is GET method
            cache_key=f'cache_{request.get_full_path()}' #creating a key

            # getting data according to the cache key if not return None
            response=cache.get(cache_key) 

            #checking 
            if response:
                return response
            
            response=self.get_response(request)
            if response.status_code==200:

                cache.set(cache_key,response.content,timeout=300)
            return response
        

        return self.get_response(request)