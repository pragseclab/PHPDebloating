<?php

/* table/secondary_tabs.twig */
class __TwigTemplate_9eb86090c4367c498bbf471d4628931b4cc1cdd24320b8c5cd668c369b1f3193 extends Twig_Template
{
    public function __construct(Twig_Environment $env)
    {
        parent::__construct($env);

        $this->parent = false;

        $this->blocks = array(
        );
    }

    protected function doDisplay(array $context, array $blocks = array())
    {
        // line 1
        if (($this->getAttribute(($context["cfg_relation"] ?? null), "relwork", array(), "array") || ($context["is_foreign_key_supported"] ?? null))) {
            // line 2
            echo "    <ul id=\"topmenu2\">
        ";
            // line 3
            echo PhpMyAdmin\Util::getHtmlTab(array("icon" => "b_props", "link" => "tbl_structure.php", "text" => _gettext("Table structure"), "id" => "table_strucuture_id"),             // line 8
($context["url_params"] ?? null));
            echo "
        ";
            // line 9
            echo PhpMyAdmin\Util::getHtmlTab(array("icon" => "b_relations", "link" => "tbl_relation.php", "text" => _gettext("Relation view"), "id" => "table_relation_id"),             // line 14
($context["url_params"] ?? null));
            echo "
    </ul>
    <div class=\"clearfloat\"></div>
";
        }
    }

    public function getTemplateName()
    {
        return "table/secondary_tabs.twig";
    }

    public function isTraitable()
    {
        return false;
    }

    public function getDebugInfo()
    {
        return array (  30 => 14,  29 => 9,  25 => 8,  24 => 3,  21 => 2,  19 => 1,);
    }

    /** @deprecated since 1.27 (to be removed in 2.0). Use getSourceContext() instead */
    public function getSource()
    {
        @trigger_error('The '.__METHOD__.' method is deprecated since version 1.27 and will be removed in 2.0. Use getSourceContext() instead.', E_USER_DEPRECATED);

        return $this->getSourceContext()->getCode();
    }

    public function getSourceContext()
    {
        return new Twig_Source("", "table/secondary_tabs.twig", "/var/www/html/phpMyAdmin-4.8.0.1-all-languages/templates/table/secondary_tabs.twig");
    }
}
