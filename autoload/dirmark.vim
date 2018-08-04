" File: dirmark.vim
" Author: kmnk <kmnknmk at gmail.com>
" License: MIT license

let s:cache_directory_path = "~/.cache/denite-dirmark"
let s:cache_file_name = "dirmark.json"
let s:default_group_name = "default"

function! dirmark#set_cache_directory_path(path)
  let s:cache_directory_path = a:path
endfunction

function! dirmark#get_cache_directory_path()
  return fnamemodify(s:cache_directory_path, ":p")
endfunction

function! dirmark#get_cache_file_path()
  return dirmark#get_cache_directory_path() . "/" . s:cache_file_name
endfunction

function! dirmark#set_default_group(group)
  let s:default_group_name = a:group
endfunction

function! dirmark#get_default_group()
  return s:default_group_name
endfunction
