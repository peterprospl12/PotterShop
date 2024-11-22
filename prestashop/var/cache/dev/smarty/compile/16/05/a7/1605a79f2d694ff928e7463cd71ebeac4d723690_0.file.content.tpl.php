<?php
/* Smarty version 3.1.48, created on 2024-11-22 11:36:30
  from '/var/www/html/admin995ruwxnq/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_67405eae95c2b3_56969535',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '1605a79f2d694ff928e7463cd71ebeac4d723690' => 
    array (
      0 => '/var/www/html/admin995ruwxnq/themes/default/template/content.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_67405eae95c2b3_56969535 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
