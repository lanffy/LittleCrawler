
CC =	cc
CFLAGS =  -pipe  -O -Wall -Wextra -Wpointer-arith -Wconditional-uninitialized -Wno-unused-parameter -Wno-deprecated-declarations -Werror -g 
CPP =	cc -E
LINK =	$(CC)


ALL_INCS = -I src/core \
	-I src/event \
	-I src/event/modules \
	-I src/os/unix \
	-I /usr/local/include \
	-I /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile \
	-I src/http \
	-I src/http/modules


CORE_DEPS = src/core/nginx.h \
	src/core/ngx_config.h \
	src/core/ngx_core.h \
	src/core/ngx_log.h \
	src/core/ngx_palloc.h \
	src/core/ngx_array.h \
	src/core/ngx_list.h \
	src/core/ngx_hash.h \
	src/core/ngx_buf.h \
	src/core/ngx_queue.h \
	src/core/ngx_string.h \
	src/core/ngx_parse.h \
	src/core/ngx_parse_time.h \
	src/core/ngx_inet.h \
	src/core/ngx_file.h \
	src/core/ngx_crc.h \
	src/core/ngx_crc32.h \
	src/core/ngx_murmurhash.h \
	src/core/ngx_md5.h \
	src/core/ngx_sha1.h \
	src/core/ngx_rbtree.h \
	src/core/ngx_radix_tree.h \
	src/core/ngx_rwlock.h \
	src/core/ngx_slab.h \
	src/core/ngx_times.h \
	src/core/ngx_shmtx.h \
	src/core/ngx_connection.h \
	src/core/ngx_cycle.h \
	src/core/ngx_conf_file.h \
	src/core/ngx_module.h \
	src/core/ngx_resolver.h \
	src/core/ngx_open_file_cache.h \
	src/core/ngx_crypt.h \
	src/core/ngx_proxy_protocol.h \
	src/core/ngx_syslog.h \
	src/event/ngx_event.h \
	src/event/ngx_event_timer.h \
	src/event/ngx_event_posted.h \
	src/event/ngx_event_connect.h \
	src/event/ngx_event_pipe.h \
	src/os/unix/ngx_time.h \
	src/os/unix/ngx_errno.h \
	src/os/unix/ngx_alloc.h \
	src/os/unix/ngx_files.h \
	src/os/unix/ngx_channel.h \
	src/os/unix/ngx_shmem.h \
	src/os/unix/ngx_process.h \
	src/os/unix/ngx_setaffinity.h \
	src/os/unix/ngx_setproctitle.h \
	src/os/unix/ngx_atomic.h \
	src/os/unix/ngx_gcc_atomic_x86.h \
	src/os/unix/ngx_thread.h \
	src/os/unix/ngx_socket.h \
	src/os/unix/ngx_os.h \
	src/os/unix/ngx_user.h \
	src/os/unix/ngx_dlopen.h \
	src/os/unix/ngx_process_cycle.h \
	src/os/unix/ngx_darwin_config.h \
	src/os/unix/ngx_darwin.h \
	src/core/ngx_regex.h \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_auto_config.h


CORE_INCS = -I src/core \
	-I src/event \
	-I src/event/modules \
	-I src/os/unix \
	-I /usr/local/include \
	-I /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile


HTTP_DEPS = src/http/ngx_http.h \
	src/http/ngx_http_request.h \
	src/http/ngx_http_config.h \
	src/http/ngx_http_core_module.h \
	src/http/ngx_http_cache.h \
	src/http/ngx_http_variables.h \
	src/http/ngx_http_script.h \
	src/http/ngx_http_upstream.h \
	src/http/ngx_http_upstream_round_robin.h \
	src/http/modules/ngx_http_ssi_filter_module.h


HTTP_INCS = -I src/http \
	-I src/http/modules


build:	binary modules manpage

binary:	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/nginx

/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/nginx:	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/nginx.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_log.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_palloc.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_array.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_list.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_hash.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_buf.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_queue.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_output_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_string.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse_time.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_inet.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_file.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crc32.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_murmurhash.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_md5.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_sha1.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rbtree.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_radix_tree.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_slab.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_times.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_shmtx.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_connection.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cycle.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_spinlock.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rwlock.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cpuinfo.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_conf_file.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_resolver.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_open_file_cache.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crypt.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_proxy_protocol.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_syslog.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_timer.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_posted.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_accept.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_connect.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_pipe.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_time.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_errno.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_alloc.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_files.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_socket.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_recv.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_readv_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_recv.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_send.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_writev_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_send.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_sendmsg_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_channel.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_shmem.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_daemon.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setaffinity.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setproctitle.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_posix_init.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_user.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_dlopen.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process_cycle.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_init.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/modules/ngx_kqueue_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_sendfile_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_regex.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_core_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_special_response.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_parse.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_log_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request_body.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_variables.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_script.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream_round_robin.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_file_cache.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_write_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_header_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_chunked_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_range_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_gzip_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_postpone_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_ssi_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_charset_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_userid_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_headers_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_copy_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_not_modified_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_static_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_autoindex_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_index_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_mirror_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_try_files_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_auth_basic_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_access_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_conn_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_req_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_geo_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_map_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_split_clients_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_referer_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_rewrite_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_proxy_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_fastcgi_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_uwsgi_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_scgi_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_memcached_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_empty_gif_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_browser_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_hash_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_ip_hash_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_least_conn_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_keepalive_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_zone_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_modules.o

	$(LINK) -o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/nginx \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/nginx.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_log.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_palloc.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_array.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_list.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_hash.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_buf.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_queue.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_output_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_string.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse_time.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_inet.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_file.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crc32.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_murmurhash.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_md5.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_sha1.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rbtree.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_radix_tree.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_slab.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_times.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_shmtx.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_connection.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cycle.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_spinlock.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rwlock.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cpuinfo.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_conf_file.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_resolver.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_open_file_cache.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crypt.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_proxy_protocol.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_syslog.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_timer.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_posted.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_accept.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_connect.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_pipe.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_time.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_errno.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_alloc.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_files.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_socket.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_recv.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_readv_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_recv.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_send.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_writev_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_send.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_sendmsg_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_channel.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_shmem.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_daemon.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setaffinity.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setproctitle.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_posix_init.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_user.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_dlopen.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process_cycle.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_init.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/modules/ngx_kqueue_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_sendfile_chain.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_regex.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_core_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_special_response.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_parse.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_log_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request_body.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_variables.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_script.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream_round_robin.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_file_cache.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_write_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_header_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_chunked_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_range_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_gzip_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_postpone_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_ssi_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_charset_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_userid_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_headers_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_copy_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_not_modified_filter_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_static_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_autoindex_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_index_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_mirror_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_try_files_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_auth_basic_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_access_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_conn_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_req_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_geo_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_map_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_split_clients_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_referer_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_rewrite_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_proxy_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_fastcgi_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_uwsgi_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_scgi_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_memcached_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_empty_gif_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_browser_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_hash_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_ip_hash_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_least_conn_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_keepalive_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_zone_module.o \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_modules.o \
	-L/usr/local/lib -lpcre -lz
	


modules:

/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_modules.o:	$(CORE_DEPS) \
	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_modules.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_modules.o \
		/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_modules.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/nginx.o:	$(CORE_DEPS) \
	src/core/nginx.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/nginx.o \
		src/core/nginx.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_log.o:	$(CORE_DEPS) \
	src/core/ngx_log.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_log.o \
		src/core/ngx_log.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_palloc.o:	$(CORE_DEPS) \
	src/core/ngx_palloc.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_palloc.o \
		src/core/ngx_palloc.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_array.o:	$(CORE_DEPS) \
	src/core/ngx_array.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_array.o \
		src/core/ngx_array.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_list.o:	$(CORE_DEPS) \
	src/core/ngx_list.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_list.o \
		src/core/ngx_list.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_hash.o:	$(CORE_DEPS) \
	src/core/ngx_hash.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_hash.o \
		src/core/ngx_hash.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_buf.o:	$(CORE_DEPS) \
	src/core/ngx_buf.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_buf.o \
		src/core/ngx_buf.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_queue.o:	$(CORE_DEPS) \
	src/core/ngx_queue.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_queue.o \
		src/core/ngx_queue.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_output_chain.o:	$(CORE_DEPS) \
	src/core/ngx_output_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_output_chain.o \
		src/core/ngx_output_chain.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_string.o:	$(CORE_DEPS) \
	src/core/ngx_string.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_string.o \
		src/core/ngx_string.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse.o:	$(CORE_DEPS) \
	src/core/ngx_parse.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse.o \
		src/core/ngx_parse.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse_time.o:	$(CORE_DEPS) \
	src/core/ngx_parse_time.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_parse_time.o \
		src/core/ngx_parse_time.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_inet.o:	$(CORE_DEPS) \
	src/core/ngx_inet.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_inet.o \
		src/core/ngx_inet.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_file.o:	$(CORE_DEPS) \
	src/core/ngx_file.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_file.o \
		src/core/ngx_file.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crc32.o:	$(CORE_DEPS) \
	src/core/ngx_crc32.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crc32.o \
		src/core/ngx_crc32.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_murmurhash.o:	$(CORE_DEPS) \
	src/core/ngx_murmurhash.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_murmurhash.o \
		src/core/ngx_murmurhash.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_md5.o:	$(CORE_DEPS) \
	src/core/ngx_md5.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_md5.o \
		src/core/ngx_md5.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_sha1.o:	$(CORE_DEPS) \
	src/core/ngx_sha1.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_sha1.o \
		src/core/ngx_sha1.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rbtree.o:	$(CORE_DEPS) \
	src/core/ngx_rbtree.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rbtree.o \
		src/core/ngx_rbtree.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_radix_tree.o:	$(CORE_DEPS) \
	src/core/ngx_radix_tree.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_radix_tree.o \
		src/core/ngx_radix_tree.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_slab.o:	$(CORE_DEPS) \
	src/core/ngx_slab.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_slab.o \
		src/core/ngx_slab.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_times.o:	$(CORE_DEPS) \
	src/core/ngx_times.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_times.o \
		src/core/ngx_times.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_shmtx.o:	$(CORE_DEPS) \
	src/core/ngx_shmtx.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_shmtx.o \
		src/core/ngx_shmtx.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_connection.o:	$(CORE_DEPS) \
	src/core/ngx_connection.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_connection.o \
		src/core/ngx_connection.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cycle.o:	$(CORE_DEPS) \
	src/core/ngx_cycle.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cycle.o \
		src/core/ngx_cycle.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_spinlock.o:	$(CORE_DEPS) \
	src/core/ngx_spinlock.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_spinlock.o \
		src/core/ngx_spinlock.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rwlock.o:	$(CORE_DEPS) \
	src/core/ngx_rwlock.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_rwlock.o \
		src/core/ngx_rwlock.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cpuinfo.o:	$(CORE_DEPS) \
	src/core/ngx_cpuinfo.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_cpuinfo.o \
		src/core/ngx_cpuinfo.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_conf_file.o:	$(CORE_DEPS) \
	src/core/ngx_conf_file.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_conf_file.o \
		src/core/ngx_conf_file.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_module.o:	$(CORE_DEPS) \
	src/core/ngx_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_module.o \
		src/core/ngx_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_resolver.o:	$(CORE_DEPS) \
	src/core/ngx_resolver.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_resolver.o \
		src/core/ngx_resolver.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_open_file_cache.o:	$(CORE_DEPS) \
	src/core/ngx_open_file_cache.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_open_file_cache.o \
		src/core/ngx_open_file_cache.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crypt.o:	$(CORE_DEPS) \
	src/core/ngx_crypt.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_crypt.o \
		src/core/ngx_crypt.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_proxy_protocol.o:	$(CORE_DEPS) \
	src/core/ngx_proxy_protocol.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_proxy_protocol.o \
		src/core/ngx_proxy_protocol.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_syslog.o:	$(CORE_DEPS) \
	src/core/ngx_syslog.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_syslog.o \
		src/core/ngx_syslog.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event.o:	$(CORE_DEPS) \
	src/event/ngx_event.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event.o \
		src/event/ngx_event.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_timer.o:	$(CORE_DEPS) \
	src/event/ngx_event_timer.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_timer.o \
		src/event/ngx_event_timer.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_posted.o:	$(CORE_DEPS) \
	src/event/ngx_event_posted.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_posted.o \
		src/event/ngx_event_posted.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_accept.o:	$(CORE_DEPS) \
	src/event/ngx_event_accept.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_accept.o \
		src/event/ngx_event_accept.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_connect.o:	$(CORE_DEPS) \
	src/event/ngx_event_connect.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_connect.o \
		src/event/ngx_event_connect.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_pipe.o:	$(CORE_DEPS) \
	src/event/ngx_event_pipe.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/ngx_event_pipe.o \
		src/event/ngx_event_pipe.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_time.o:	$(CORE_DEPS) \
	src/os/unix/ngx_time.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_time.o \
		src/os/unix/ngx_time.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_errno.o:	$(CORE_DEPS) \
	src/os/unix/ngx_errno.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_errno.o \
		src/os/unix/ngx_errno.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_alloc.o:	$(CORE_DEPS) \
	src/os/unix/ngx_alloc.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_alloc.o \
		src/os/unix/ngx_alloc.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_files.o:	$(CORE_DEPS) \
	src/os/unix/ngx_files.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_files.o \
		src/os/unix/ngx_files.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_socket.o:	$(CORE_DEPS) \
	src/os/unix/ngx_socket.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_socket.o \
		src/os/unix/ngx_socket.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_recv.o:	$(CORE_DEPS) \
	src/os/unix/ngx_recv.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_recv.o \
		src/os/unix/ngx_recv.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_readv_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_readv_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_readv_chain.o \
		src/os/unix/ngx_readv_chain.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_recv.o:	$(CORE_DEPS) \
	src/os/unix/ngx_udp_recv.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_recv.o \
		src/os/unix/ngx_udp_recv.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_send.o:	$(CORE_DEPS) \
	src/os/unix/ngx_send.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_send.o \
		src/os/unix/ngx_send.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_writev_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_writev_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_writev_chain.o \
		src/os/unix/ngx_writev_chain.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_send.o:	$(CORE_DEPS) \
	src/os/unix/ngx_udp_send.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_send.o \
		src/os/unix/ngx_udp_send.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_sendmsg_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_udp_sendmsg_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_udp_sendmsg_chain.o \
		src/os/unix/ngx_udp_sendmsg_chain.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_channel.o:	$(CORE_DEPS) \
	src/os/unix/ngx_channel.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_channel.o \
		src/os/unix/ngx_channel.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_shmem.o:	$(CORE_DEPS) \
	src/os/unix/ngx_shmem.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_shmem.o \
		src/os/unix/ngx_shmem.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process.o:	$(CORE_DEPS) \
	src/os/unix/ngx_process.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process.o \
		src/os/unix/ngx_process.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_daemon.o:	$(CORE_DEPS) \
	src/os/unix/ngx_daemon.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_daemon.o \
		src/os/unix/ngx_daemon.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setaffinity.o:	$(CORE_DEPS) \
	src/os/unix/ngx_setaffinity.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setaffinity.o \
		src/os/unix/ngx_setaffinity.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setproctitle.o:	$(CORE_DEPS) \
	src/os/unix/ngx_setproctitle.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_setproctitle.o \
		src/os/unix/ngx_setproctitle.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_posix_init.o:	$(CORE_DEPS) \
	src/os/unix/ngx_posix_init.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_posix_init.o \
		src/os/unix/ngx_posix_init.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_user.o:	$(CORE_DEPS) \
	src/os/unix/ngx_user.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_user.o \
		src/os/unix/ngx_user.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_dlopen.o:	$(CORE_DEPS) \
	src/os/unix/ngx_dlopen.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_dlopen.o \
		src/os/unix/ngx_dlopen.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process_cycle.o:	$(CORE_DEPS) \
	src/os/unix/ngx_process_cycle.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_process_cycle.o \
		src/os/unix/ngx_process_cycle.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_init.o:	$(CORE_DEPS) \
	src/os/unix/ngx_darwin_init.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_init.o \
		src/os/unix/ngx_darwin_init.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/modules/ngx_kqueue_module.o:	$(CORE_DEPS) \
	src/event/modules/ngx_kqueue_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/event/modules/ngx_kqueue_module.o \
		src/event/modules/ngx_kqueue_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_sendfile_chain.o:	$(CORE_DEPS) \
	src/os/unix/ngx_darwin_sendfile_chain.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/os/unix/ngx_darwin_sendfile_chain.o \
		src/os/unix/ngx_darwin_sendfile_chain.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_regex.o:	$(CORE_DEPS) \
	src/core/ngx_regex.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/core/ngx_regex.o \
		src/core/ngx_regex.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http.o \
		src/http/ngx_http.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_core_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_core_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_core_module.o \
		src/http/ngx_http_core_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_special_response.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_special_response.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_special_response.o \
		src/http/ngx_http_special_response.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_request.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request.o \
		src/http/ngx_http_request.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_parse.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_parse.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_parse.o \
		src/http/ngx_http_parse.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_log_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_log_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_log_module.o \
		src/http/modules/ngx_http_log_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request_body.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_request_body.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_request_body.o \
		src/http/ngx_http_request_body.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_variables.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_variables.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_variables.o \
		src/http/ngx_http_variables.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_script.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_script.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_script.o \
		src/http/ngx_http_script.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_upstream.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream.o \
		src/http/ngx_http_upstream.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream_round_robin.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_upstream_round_robin.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_upstream_round_robin.o \
		src/http/ngx_http_upstream_round_robin.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_file_cache.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_file_cache.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_file_cache.o \
		src/http/ngx_http_file_cache.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_write_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_write_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_write_filter_module.o \
		src/http/ngx_http_write_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_header_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_header_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_header_filter_module.o \
		src/http/ngx_http_header_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_chunked_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_chunked_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_chunked_filter_module.o \
		src/http/modules/ngx_http_chunked_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_range_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_range_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_range_filter_module.o \
		src/http/modules/ngx_http_range_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_gzip_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_gzip_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_gzip_filter_module.o \
		src/http/modules/ngx_http_gzip_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_postpone_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_postpone_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_postpone_filter_module.o \
		src/http/ngx_http_postpone_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_ssi_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_ssi_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_ssi_filter_module.o \
		src/http/modules/ngx_http_ssi_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_charset_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_charset_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_charset_filter_module.o \
		src/http/modules/ngx_http_charset_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_userid_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_userid_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_userid_filter_module.o \
		src/http/modules/ngx_http_userid_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_headers_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_headers_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_headers_filter_module.o \
		src/http/modules/ngx_http_headers_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_copy_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/ngx_http_copy_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/ngx_http_copy_filter_module.o \
		src/http/ngx_http_copy_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_not_modified_filter_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_not_modified_filter_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_not_modified_filter_module.o \
		src/http/modules/ngx_http_not_modified_filter_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_static_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_static_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_static_module.o \
		src/http/modules/ngx_http_static_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_autoindex_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_autoindex_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_autoindex_module.o \
		src/http/modules/ngx_http_autoindex_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_index_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_index_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_index_module.o \
		src/http/modules/ngx_http_index_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_mirror_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_mirror_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_mirror_module.o \
		src/http/modules/ngx_http_mirror_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_try_files_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_try_files_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_try_files_module.o \
		src/http/modules/ngx_http_try_files_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_auth_basic_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_auth_basic_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_auth_basic_module.o \
		src/http/modules/ngx_http_auth_basic_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_access_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_access_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_access_module.o \
		src/http/modules/ngx_http_access_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_conn_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_limit_conn_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_conn_module.o \
		src/http/modules/ngx_http_limit_conn_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_req_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_limit_req_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_limit_req_module.o \
		src/http/modules/ngx_http_limit_req_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_geo_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_geo_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_geo_module.o \
		src/http/modules/ngx_http_geo_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_map_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_map_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_map_module.o \
		src/http/modules/ngx_http_map_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_split_clients_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_split_clients_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_split_clients_module.o \
		src/http/modules/ngx_http_split_clients_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_referer_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_referer_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_referer_module.o \
		src/http/modules/ngx_http_referer_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_rewrite_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_rewrite_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_rewrite_module.o \
		src/http/modules/ngx_http_rewrite_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_proxy_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_proxy_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_proxy_module.o \
		src/http/modules/ngx_http_proxy_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_fastcgi_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_fastcgi_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_fastcgi_module.o \
		src/http/modules/ngx_http_fastcgi_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_uwsgi_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_uwsgi_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_uwsgi_module.o \
		src/http/modules/ngx_http_uwsgi_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_scgi_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_scgi_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_scgi_module.o \
		src/http/modules/ngx_http_scgi_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_memcached_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_memcached_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_memcached_module.o \
		src/http/modules/ngx_http_memcached_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_empty_gif_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_empty_gif_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_empty_gif_module.o \
		src/http/modules/ngx_http_empty_gif_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_browser_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_browser_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_browser_module.o \
		src/http/modules/ngx_http_browser_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_hash_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_hash_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_hash_module.o \
		src/http/modules/ngx_http_upstream_hash_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_ip_hash_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_ip_hash_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_ip_hash_module.o \
		src/http/modules/ngx_http_upstream_ip_hash_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_least_conn_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_least_conn_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_least_conn_module.o \
		src/http/modules/ngx_http_upstream_least_conn_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_keepalive_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_keepalive_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_keepalive_module.o \
		src/http/modules/ngx_http_upstream_keepalive_module.c


/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_zone_module.o:	$(CORE_DEPS) $(HTTP_DEPS) \
	src/http/modules/ngx_http_upstream_zone_module.c
	$(CC) -c $(CFLAGS) $(CORE_INCS) $(HTTP_INCS) \
		-o /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/src/http/modules/ngx_http_upstream_zone_module.o \
		src/http/modules/ngx_http_upstream_zone_module.c


manpage:	/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/nginx.8

/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/nginx.8:	man/nginx.8 /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/ngx_auto_config.h
	sed -e "s|%%PREFIX%%|/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app|" \
		-e "s|%%PID_PATH%%|/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs/nginx.pid|" \
		-e "s|%%CONF_PATH%%|/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/nginx.conf|" \
		-e "s|%%ERROR_LOG_PATH%%|/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs/error.log|" \
		< man/nginx.8 > $@

install:	build 
	test -d '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app' || mkdir -p '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app'

	test -d '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/sbin' \
		|| mkdir -p '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/sbin'
	test ! -f '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/sbin/nginx' \
		|| mv '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/sbin/nginx' \
			'$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/sbin/nginx.old'
	cp /Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-compile/nginx '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/sbin/nginx'

	test -d '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf' \
		|| mkdir -p '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'

	cp conf/koi-win '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'
	cp conf/koi-utf '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'
	cp conf/win-utf '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'

	test -f '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/mime.types' \
		|| cp conf/mime.types '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'
	cp conf/mime.types '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/mime.types.default'

	test -f '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/fastcgi_params' \
		|| cp conf/fastcgi_params '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'
	cp conf/fastcgi_params \
		'$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/fastcgi_params.default'

	test -f '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/fastcgi.conf' \
		|| cp conf/fastcgi.conf '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'
	cp conf/fastcgi.conf '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/fastcgi.conf.default'

	test -f '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/uwsgi_params' \
		|| cp conf/uwsgi_params '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'
	cp conf/uwsgi_params \
		'$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/uwsgi_params.default'

	test -f '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/scgi_params' \
		|| cp conf/scgi_params '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf'
	cp conf/scgi_params \
		'$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/scgi_params.default'

	test -f '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/nginx.conf' \
		|| cp conf/nginx.conf '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/nginx.conf'
	cp conf/nginx.conf '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/conf/nginx.conf.default'

	test -d '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs' \
		|| mkdir -p '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs'

	test -d '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs' \
		|| mkdir -p '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs'

	test -d '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/html' \
		|| cp -R html '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app'

	test -d '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs' \
		|| mkdir -p '$(DESTDIR)/Users/rlanffy/Documents/githubPro/LittleCrawler/nginx-app/logs'
