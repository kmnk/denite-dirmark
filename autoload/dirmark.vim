" File: dirmark.vim
" Author: kmnk <kmnknmk at gmail.com>
" License: MIT license

let s:data_directory_path = "~/.cache/denite-dirmark"
let s:data_file_name = "dirmark.json"
let s:default_group_name = "default"

function! dirmark#set_data_directory_path(path)
  let s:data_directory_path = a:path
endfunction

function! dirmark#get_data_directory_path()
  return fnamemodify(s:data_directory_path, ":p")
endfunction

function! dirmark#get_data_file_path()
  return dirmark#get_data_directory_path() . "/" . s:data_file_name
endfunction

function! dirmark#set_cache_directory_path(path)
  echohl WarningMsg | echomsg 'dirmark#set_cache_directory_path is deprecated. use dirmark#set_data_directory_path' | echohl None
  call dirmark#set_data_directory_path(a:path)
endfunction

function! dirmark#get_cache_directory_path()
  echohl WarningMsg | echomsg 'dirmark#get_cache_directory_path is deprecated. use dirmark#get_data_directory_path' | echohl None
  return dirmark#get_data_directory_path()
endfunction

function! dirmark#get_cache_file_path()
  echohl WarningMsg | echomsg 'dirdirmark#get_cache_file_path is deprecated. use dirmark#get_data_file_path' | echohl None
  return dirmark#get_data_file_path()
endfunction

function! dirmark#set_default_group(group)
  let s:default_group_name = a:group
endfunction

function! dirmark#get_default_group()
  return s:default_group_name
endfunction
