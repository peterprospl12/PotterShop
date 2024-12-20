{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License 3.0 (AFL-3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}
<div class="col-md-6 links gray-long-line" style="width:100%">
  <div class="row">
    {foreach $linkBlocks as $linkBlock}
      <div class="col-md-6 wrapper linkblock-heading"
        style="width: calc(100% / 6); padding-left: 5px; padding-right: 5px;">
        <p class="h3 hidden-sm-down harry-potter-font-class">{$linkBlock.title}</p>
        <div class="title clearfix hidden-md-up" data-target="#footer_sub_menu_{$linkBlock.id}" data-toggle="collapse">
          <span class="h3">{$linkBlock.title}</span>
          <span class="float-xs-right">
            <span class="navbar-toggler collapse-icons">
              <i class="material-icons add">&#xE313;</i>
              <i class="material-icons remove">&#xE316;</i>
            </span>
          </span>
        </div>
        <ul id="footer_sub_menu_{$linkBlock.id}" class="collapse">
          {foreach $linkBlock.links as $link}
            <li style="line-height: 30px;">
              <a class="underline-link" id="{$link.id}-{$linkBlock.id}" class="{$link.class}" href="{$link.url}"
                title="{$link.description}" {if !empty($link.target)} target="{$link.target}" {/if}>
                {if $link.title == 'Nowe produkty'}
                  Nowości
                {else}
                  {$link.title}
                {/if}
              </a>
            </li>
          {/foreach}
        </ul>
      </div>
    {/foreach}
  </div>
  <hr style="height: 1px; background-color: #757575;; border: none; margin: 0;">
</div>