#  Copyright 2007 GRAHAM DUMPLETON
# 
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

APXS = /opt/local/bin/apxs
PYTHON = python

DESTDIR =
LIBEXECDIR = /opt/local/lib/apache2/modules

CPPFLAGS =    
CFLAGS =   -Wc,'-arch arm64'
LDFLAGS =  -Wl,-F -framework    -arch arm64
LDLIBS =    

all : mod_wsgi.la

mod_wsgi.la : mod_wsgi.c
	$(APXS) -c $(CPPFLAGS) $(CFLAGS) mod_wsgi.c $(LDFLAGS) $(LDLIBS)

$(DESTDIR)$(LIBEXECDIR) :
	mkdir -p $@

install : all $(DESTDIR)$(LIBEXECDIR)
	$(APXS) -i -S LIBEXECDIR=$(DESTDIR)$(LIBEXECDIR) -n 'mod_wsgi' mod_wsgi.la

clean :
	-rm -rf .libs
	-rm -f mod_wsgi.o mod_wsgi.la mod_wsgi.lo mod_wsgi.slo mod_wsgi.loT
	-rm -f config.log config.status
	-rm -rf autom4te.cache

distclean : clean
	-rm -f Makefile Makefile.in

realclean : distclean
	-rm -f configure
